#!/usr/bin/env python

"""
This application uses WxPython for:
- control widgets to define the camera (perspective)
- and to manipulate the scene (3D shapes),
- a Paint display for the 2D rendering.
"""

import sys
import os

import scene
import myapp
import config

# forces static loading to please py2app/py/exe:
try:
    import reportlab.rl_settings
except:
    pass

defaults = {
    "camera_azimuth": 70,
    "camera_altitude": 32,
    "camera_distance": 800,
    "camera_fov": 80,
    "cone_radius": 210,
    "cone_height": 297,
    "plane_tilt": 0,
    "export_bitmap_width": 1600,
    "export_bitmap_height": 2262,
    "export_bitmap": None,
    "export_pdf": None,
}

scene = scene.Scene()

# go to the dir representing the current module
try:
    my_dir = os.path.split(__file__)[0]
    os.chdir(my_dir)
except:
    try:
        my_dir = os.path.split(sys.argv[0])[0]
        my_dir = os.path.join(my_dir, "conedevelopment_files")
        os.chdir(my_dir)
    except:
        my_dir = os.path.split(sys.argv[0])[0]
        os.chdir(my_dir)

# start app
myapp.run_gui(defaults, scene)

