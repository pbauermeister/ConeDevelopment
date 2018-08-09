# A. Copyright

ConeDevelopment (https://github.com/pbauermeister/ConeDevelopment)
(C) copyright 2018 P. Bauermeister.

# B. License

ConeDevelopment is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.

ConeDevelopment is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details. You should have received a
copy of the GNU General Public License along with ConeDevelopment; if not,
write to the Free Software Foundation, Inc., 59 Temple Place, Suite
330, Boston, MA 02111-1307 USA.## Credits and Copyright

# C. Third-party software with portions embedded into the run-time

## Python 2.7
- An interpreted, general-purpose high-level programming language whose design
  philosophy emphasizes code readability. Python aims to combine "remarkable
  power with very clear syntax", and its standard library is large and
  comprehensive. Its use of indentation for block delimiters is unusual among
  popular programming languages.

  Python supports multiple programming paradigms, primarily but not limited to
  object oriented, imperative and, to a lesser extent, functional programming
  styles. It features a fully dynamic type system and automatic memory
  management, similar to that of Scheme, Ruby, Perl, and Tcl. Like other
  dynamic languages, Python is often used as a scripting language, but is also
  used in a wide range of non-scripting contexts.
- Home:     http://www.python.org/
- Download: http://www.python.org/download/
- Usage:    The application is written in Python.


## wxPython2.8
- wxPython is a wrapper for the cross-platform GUI API (often referred
  to as a 'toolkit') wxWidgets (which is written in C++) for the
  Python programming language. It is one of the alternatives to
  Tkinter, which is bundled with Python. It is implemented as a Python
  extension module (native code). Other popular alternatives are PyGTK
  and PyQt. Like wxWidgets, wxPython is free software.
- Home:     http://wxpython.org/
- Download: http://wxpython.org/download.php#stable
- Usage:    The application's GUI is made with wxPython.


# D. Third-party software used at build-time

## Inno Setup with InnoIDE 5.4.
- Inno Setup is a free script-driven installation system created in
  CodeGear Delphi by Jordan Russell.
- Home:     http://www.InnoIDE.org and http://www.jrsoftware.org/isinfo.php
- Download: http://www.innoide.org/download.php
- Usage:    The setup EXE is built using InnoIDE.


## py2exe-0.6.9
- py2exe is a Python extension which converts Python scripts (.py)
  into Windows executables (.exe). These executables can run on a
  system without Python installed.
- Home:     http://www.py2exe.org/
- Download: http://sourceforge.net/projects/py2exe/files/
- Usage:    The application uses py2exe to make it independant from the
            Python interpreter.


## txt2tags-2.6
- txt2tags is a document generator software that uses a lightweight
  markup language. txt2tags is free software under GNU General Public
  License.

  Written in Python, it can export documents to several formats
  including: HTML, XHTML, SGML, LaTeX, Lout, roff, MediaWiki, Google
  Code Wiki, DokuWiki, MoinMoin, MagicPoint, PageMaker and plain text.
- Home:     http://txt2tags.org/
- Download: http://txt2tags.org/download.html
- Usage:    Script used at build-time to generate product README as HTML page.
