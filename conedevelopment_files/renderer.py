"""This module renders the truncated cone side as a 2D flat developement
curve.

"""
import wx
import math

from display_wx import PaintDisplay
from display_bitmap import BitmapDisplay
import geometry
import render_fullscreen
import bitmap
from gui_utils import eraseBackground
import constants
import cone_development

DEBUG = False

FILL_COLOR    = (255, 255, 255)
LINE_COLOR    = ( 64,  64,  64)
ENDLINE_COLOR = (197, 197, 197)
MARKS_COLOR   = (  0,   0, 255)

class Renderer(object):

    def __init__(self, bitmap):
        self.bitmap = bitmap
        self.bg_bmp_render = wx.Bitmap("bg_2.jpg")

    def renderCanvas(self, canvas, preview=True):
        pdc = wx.PaintDC(canvas)  # simple device context
        dc = wx.GCDC(pdc)  # device context with alpha and anti-alias
        if constants.WITH_TEXTURE_CANVAS:
            eraseBackground(canvas, dc, self.bg_bmp_render)

        canvas_w, canvas_h = canvas.GetClientSize()
        canvas_w -= 1
        canvas_h -= 1
        display = PaintDisplay(dc, canvas_w, canvas_h)
        return self.renderDisplay(display, canvas_w, canvas_h,
                                  preview=preview, box=False)

    def renderDisplay(self, display, display_w, display_h, preview, box,
                      progressPcentFn=lambda x: None):
        # retrieve cone development data
        lengths, total_angle = cone_development.get()
        n = len(lengths)

        # angle stuff
        angle_increment = total_angle / n
        angle_offset = (math.pi * 2 - total_angle) / 2

        # compute points in polar coordinates
        coloredPoints = [(0, 0, None)] # start at center
        color = ENDLINE_COLOR
        for i in range(n):
            angle = angle_increment * i + angle_offset
            x = lengths[i] * math.cos(angle)
            y = lengths[i] * math.sin(angle)
            coloredPoints.append((x, y, color))
            color = LINE_COLOR
        coloredPoints.append((0, 0, ENDLINE_COLOR)) # end at center

        # bounding box, scaling
        origin, w, h = geometry.boundingRect([(x,y) for x,y,c
                                              in coloredPoints])

        # recentering, and 90 degree rotating to fit into portrait
        factor = 1.05 # give a 5% margin
        dx = -origin[0] - w / 2
        dy = -origin[1] - h / 2
        rotated = (w < h) ^ (display_w < display_h)
        if rotated:
            display.setScale(h*factor, w*factor)
            coloredPoints = [(y+dy, x+dx, c) for x,y,c in coloredPoints]
        else:
            display.setScale(w*factor, h*factor)
            coloredPoints = [(x+dx, y+dy, c) for x,y,c in coloredPoints]

        # draw shape
        display.DrawPolygon2(coloredPoints, FILL_COLOR)

        # add origin
        #d = min(w, h) / 20
        d = min(display_w, display_h) / display.getScale() / 20
        r = d * 0.35
        if rotated:
            display.DrawCross(dy, dx, d, MARKS_COLOR)
            display.DrawCircle(dy, dx, r, MARKS_COLOR)
        else:
            display.DrawCross(dx, dy, d, MARKS_COLOR)
            display.DrawCircle(dx, dy, r, MARKS_COLOR)

        # done
        progressPcentFn(99)

    def renderCanvasHiQ(self, canvas):
        self.renderCanvas(canvas, preview=False)

    def renderScreen(self, frame):
        render_fullscreen.render(frame, self.renderCanvasHiQ)

    def renderImage(self, width, height, progressPcentFn=None):
        display = BitmapDisplay(width, height)
        self.renderDisplay(display, width, height, preview=False, box=True,
                           progressPcentFn=progressPcentFn)
        bmp = display.GetBitmap()
        return bmp
