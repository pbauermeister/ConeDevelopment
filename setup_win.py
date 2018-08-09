from distutils.core import setup
import py2exe
import ConfigParser
import os
import sys


PY2EXE_OPTIONS = {
    'bundle_files': 3,
    'dist_dir': 'output-py2exe',
    }

try:
    # run PY2EXE
    setup(
        name="ConeDevelopment.py",
        windows=['ConeDevelopment.py'],   # hides the console
        #console=['ConeDevelopment.py'],   # shows the console
        options={'py2exe': PY2EXE_OPTIONS},
        )

except:
    raw_input()  # pause on error
    raise

# done
