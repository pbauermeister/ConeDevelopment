"""
Constants of the app.
"""
import os
import sys
import glob

#DEFAULT_PATH = os.path.expanduser("~/.ConeDevelopment.cnf")

IS_WINDOWS = False
IS_OSX = False
IS_LINUX = False

if os.name == 'nt':
    print "System is Windows"
    parent = '%(APPDATA)s' % os.environ
    APP_CONFIG_PATH = os.path.join(parent, "ConeDevelopment.ini")
    IS_WINDOWS = True
    WITH_TEXTURE_BG =  False
    WITH_TEXTURE_CANVAS = False

elif sys.platform.startswith('darwin'):
    print "System is Mac"
    APP_CONFIG_PATH = os.path.expanduser("~/.ConeDevelopment.ini")
    IS_OSX = True
    WITH_TEXTURE_BG = False
    WITH_TEXTURE_CANVAS = False

elif os.name == 'posix':
    print "System is Linux/Unix"
    APP_CONFIG_PATH = os.path.expanduser("~/.ConeDevelopment.ini")
    IS_LINUX = True
    WITH_TEXTURE_BG = True
    WITH_TEXTURE_CANVAS = False

print "Program config file is", APP_CONFIG_PATH

EXTENSION                   = ".conedevelopment"
DEFERRED_REDRAW_DELAY       = 0.2

BITMAP_THUMBNAIL_SIZE       = 300
BITMAP_THUMB_TRANSPARENCY   = 0.75
MAX_REASONABLE_COORD_FACTOR = 50
