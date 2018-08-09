#!/usr/bin/env python

import os
import sys
import platform

from conedevelopment_files import version

#
# Gen version
#

print
print "= Generating version nr from SCM revision ="
version_str = version.getVersionFromScm()
version.setVersionToIni('conedevelopment_files')
print version_str

#
# Run txt2tags, for formatted README
#

print
print "= Generating html doc using text2tags ="
print "Patching version string"
basename = os.path.join("conedevelopment_files", "README")
txt = open(basename + ".txt").read().replace("@CURRENT_VERSION@", version_str)
open(basename + ".tmp", "w").write(txt)

print "Calling text2tags"
t2t_opt = ("--toc --enum-title --css-sugar --css-inside "
           "--style=README.css -o %s.html " ) % (basename)
ret = os.system("python txt2tags -t html %s %s.tmp" % (t2t_opt, basename))
if ret:
    raise RuntimeError("Command failed")

#
# Run setup
#

if os.name == "nt":
    print
    print "= Running setup for Windows ="
    import setup_win

elif sys.platform.startswith('darwin'):
    print
    print "= Running setup for OSX ="
    import setup_osx

elif platform.system() == 'Linux':
    from distutils.core import setup
    info = {
        'version': version_str,
        'description': "ConeDevelopment - Cone development visualisation tool",
        'author': "Pascal Bauermeister",
        'author_email': "pascal.bauermeister@gmail.com",
        'license': 'GPL',
        }
    info.update({
            'name': "conedevelopment",
            'scripts': ['conedevelopment'],
            'packages': ['conedevelopment_files'],
            'package_data': {'conedevelopment_files': [
                    'sample_pics/*', '*.png', '*.ic*', '*.jpg',
                    'README.html',
                    'autogenerated_version.ini',
                    ]},
            'requires': [
                'imaging (>=1.1.7)',
                'numpy (>=1.6.1)',
                'reportlab (>=2.5)',
                'simplejson (>=2.3.2)',
                'wxgtk (>=2.8.12)',
                ],
            })

    print
    print "= Running setup for Linux (Debian) ="
    try:
        setup(**info)
    except:
        print "### Setup failed. Did you install python-stdeb? ###"
        raise

else:
    raise RuntimeError("No setup yet for %s" % os.name)

print
print "Setup done."
