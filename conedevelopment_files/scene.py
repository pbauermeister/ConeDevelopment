"""
This module defines the scene, consisting of various objects.

The objects can be created or moved via object-specific functions
provided here.
"""
import math
import numpy
import traceback
import pprint

import shape
import geometry
import anamorphosis
import perspective
import cone_development

AXIS_LENGTH = 32

PLANE_FILL_COLOR      = '#fff4f4e0'
PLANE_BORDER_COLOR    = '#e00000'
INTERSECT_POINT_COLOR = '#880000'
CONE_SEGMENT_COLOR    = '#00000020'
CONE_DIAMETER_COLOR   = '#00004080'

def minmax (val, rng):
    return (
        min(val, rng[0]) if rng[0] is not None else val,
        max(val, rng[1]) if rng[1] is not None else val,
    )


class Scene(object):
    """
    The scene is essentially a list of shapes, that can be
    manipulated.
    """
    def __init__(self):
        self.plane_tilt = None
        self.camera_matrix = None

    def makeShapes(self):
        shape.clearShapes()

        # assemble scene
        axis_y = shape.Axis([0, 0, 0], [ 0, AXIS_LENGTH,  0], "y")
        axis_x = shape.Axis([0, 0, 0], [AXIS_LENGTH,  0,  0], "x")
        axis_z = shape.Axis([0, 0, 0], [ 0,  0, AXIS_LENGTH], "z")

        # normed plane
        c = math.cos(self.plane_tilt)
        s = math.sin(self.plane_tilt)
        w = 1
        h = 1
        points = [[-w * c,  w * s,  h],
                  [ w * c, -w * s,  h],
                  [ w * c, -w * s, -h],
                  [-w * c,  w * s, -h]]
        p1, p2, p3 = [numpy.array(point) for point in points[0:3]]
                
        # cut cone
        N = 360/2
        r = self.cone_radius
        h = self.cone_height
        pa = [0, h, 0] # cone summit
        
        cone_segments = []
        cone_diameter_points = []
        intersect_points = []
        intersect_zrange = [None, None]
        lengths = []

        for i in range(0, N):
            a_deg = 360. / N * i
            a = math.radians(a_deg)
            x = math.cos(a) * r
            y = math.sin(a) * r

            # pa - pb is a cone segment, cut by the floor
            pb = [x, 0, y]

            # let us extend or cut the segment until it meets the plane
            p = geometry.lineIntersectsPlane(
                numpy.array(pa), numpy.array(pb),
                p1, p2, p3)
            # - add intersection point
            intersect_points.append(
                shape.Point(p, lineColor=INTERSECT_POINT_COLOR))
            # - add segment
            cone_segments.append(shape.Segment(pa, p, CONE_SEGMENT_COLOR))
            # - segment length
            lengths.append(numpy.linalg.norm(p-pa))
            # - lateral extrema (along z)
            intersect_zrange = minmax(p[2], intersect_zrange)

            # - add cone diameter point, when above plane (= intersect
            #   is below floor)
            if p[1] < 0:
                cone_diameter_points.append(
                    shape.Point(pb, lineColor=CONE_DIAMETER_COLOR))
            
        # longitudinal extrema (along x)
        dists = []
        for x,y in ((r, 0), (-r, 0)):
            pb = [x, 0, y]
            p = geometry.lineIntersectsPlane(
                numpy.array(pa), numpy.array(pb),
                p1, p2, p3)
            d = math.sqrt(p[0]*p[0] + p[1]*p[1] + p[2]*p[2])
            dists.append(min(d, 1500))
        
        # plane enclosing intersect
        x1, x0 = dists[0], -dists[1]
        z0, z1 = intersect_zrange
        c2 = math.cos(self.plane_tilt)
        s2 = math.sin(self.plane_tilt)
        points = [[x0 * c2, -x0 * s2, z0],
                  [x1 * c2, -x1 * s2, z0],
                  [x1 * c2, -x1 * s2, z1],
                  [x0 * c2, -x0 * s2, z1]]
        plane_shapes = [shape.Face(points, name="plane",
                                   fillColor=PLANE_FILL_COLOR,
                                   lineColor=PLANE_BORDER_COLOR)]

        # store intersect points
        cone_development_total_angle = math.pi * 2 * r / math.sqrt(h*h + r*r)
        cone_development.set(lengths, cone_development_total_angle)
        
        # poor man's hidden parts: by ordering the objects dep. on dot
        # product between the plane normal and the camera direction
        plane_vect1 = p2 - p1
        plane_vect2 = p3 - p1
        plane_normal = numpy.cross(plane_vect1, plane_vect2)
        dot_prod = numpy.dot(plane_normal, self.camera_pos)

        tilted = self.plane_tilt < 0
        axes1 = [axis_x] if tilted else []
        axes2 = [axis_y] if tilted else [axis_x, axis_y]

        if dot_prod >= 0:
            return (axes1
                    + plane_shapes
                    + axes2 + [axis_z]
                    + cone_segments + cone_diameter_points
                    + intersect_points)
        else:
            return (cone_segments + cone_diameter_points
                    + axes2
                    + plane_shapes
                    + axes1 + [axis_z]
                    + intersect_points)


        # done
        return scene

    def setCameraPos(self, camera_pos):
        self.camera_pos = camera_pos

    def render(self, display, getValueFn, setPosFn):
        # camera pos indication
        if setPosFn is not None:
            theta = math.radians(90 - getValueFn("camera_altitude"))
            phi = math.radians(90 - getValueFn("camera_azimuth"))
            r = getValueFn("camera_distance")
            y = r * math.cos(theta)
            x = r * math.cos(phi) * math.sin(theta)
            z = r * math.sin(phi) * math.sin(theta)
            pos = "x:%d  y:%d  z:%d" % (x, y, z)
            setPosFn(pos)
    
        # create perspective
        persp = perspective.Perspective(
            getValueFn("camera_azimuth"),
            getValueFn("camera_altitude"),
            getValueFn("camera_distance"),
            getValueFn("camera_fov"))

        # Cone
        self.cone_height = getValueFn("cone_height")
        self.cone_radius = getValueFn("cone_radius")
        self.plane_tilt = math.radians(getValueFn("plane_tilt"))

        # camera
        self.camera_altitude = getValueFn("camera_altitude")        
        self.setCameraPos(persp.getCamera())
    
        # compute 3D -> 2D
        shapes = self.makeShapes()
        for each in shapes:
            if each is None:
                continue
            show = True
            try:
                each.render(display, persp, show=show)
            except ValueError, e:
                traceback.print_exc()
                print e
                pass  # some point cannot be rendered
            except OverflowError, e:
                traceback.print_exc()
                print e
                pass  # some point cannot be rendered
        return
