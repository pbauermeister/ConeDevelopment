# ConeDevelopment

(C) by Pascal Bauermeister, 2018.

## Purpose =

ConeDevelopment is an interactive program to explore the development
of a truncated cone.

Truncating a cone by a plane results in second degree curves in the
truncation plane. But what about the curve when you develop the
surface of the truncated cone?

Surprisingly these curves are not so obvious or trivial.  See
[this picture](https://slideplayer.com/slide/5256991/16/images/20/Q+15.26:+A+right+circular+cone+base+30+mm+side+and+height+50+mm+rests+on+its+base+on+H.P.+It+is+cut+by+a+section+plane+perpendicular+to+the+V.P.,+inclined+at+45%C2%BA+to+the+H.P.+and+bisecting+the+axis.+Draw+the+projections+of+the+truncated+cone+and+develop+its+lateral+surface..jpg).

This program lets you explore the question by computing the curve
numerically. One can modify the cone shape and plane angle as desired
and see the resulting development curve.

This program was based on another more complex program,
https://github.com/pbauermeister/Anamorphy. That is why (1) in the
source code there may be remains of the original program, and (2) it
is still in Python 2.x.

I would be interested in any analytical solution (as opposed to the
very overkill numerical solution proposed here). You can kindly
contact me (or post a github ticket) for any hint.

This program was inspired by an interesting discussion with Mr. Udo
Bund, my wife's uncle. It was about the construction of a cap to fit
on the nozzle of a high-pressure Kaercher cleaner in order to reduce
the peripheral projections.

## License

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
330, Boston, MA 02111-1307 USA.

## History 

- 2018-08-09 Initial release


## How to Get the Sources

See https://github.com/pbauermeister/ConeDevelopment

## Credits and Copyright

(C) copyright 2018 P. Bauermeister.


## Third-party software with portions embedded into the run-time

### Python 2.7
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


### wxPython2.8
- wxPython is a wrapper for the cross-platform GUI API (often referred
  to as a 'toolkit') wxWidgets (which is written in C++) for the
  Python programming language. It is one of the alternatives to
  Tkinter, which is bundled with Python. It is implemented as a Python
  extension module (native code). Other popular alternatives are PyGTK
  and PyQt. Like wxWidgets, wxPython is free software.
- Home:     http://wxpython.org/
- Download: http://wxpython.org/download.php#stable
- Usage:    The application's GUI is made with wxPython.


## Third-party software used at build-time

### Inno Setup with InnoIDE 5.4.
- Inno Setup is a free script-driven installation system created in
  CodeGear Delphi by Jordan Russell.
- Home:     http://www.InnoIDE.org and http://www.jrsoftware.org/isinfo.php
- Download: http://www.innoide.org/download.php
- Usage:    The setup EXE is built using InnoIDE.


### py2exe-0.6.9
- py2exe is a Python extension which converts Python scripts (.py)
  into Windows executables (.exe). These executables can run on a
  system without Python installed.
- Home:     http://www.py2exe.org/
- Download: http://sourceforge.net/projects/py2exe/files/
- Usage:    The application uses py2exe to make it independant from the
            Python interpreter.


### wxGlade 0.6.3
- wxGlade is a program for creating wxWidgets GUIs. It can generate layout code
  for C++, Python and Perl.
- Home:     http://wxglade.sourceforge.net/
- Download: http://sourceforge.net/projects/wxglade/
- Usage:    exGlade is used to design and maintain the GUI of the application.


### txt2tags-2.6
- txt2tags is a document generator software that uses a lightweight
  markup language. txt2tags is free software under GNU General Public
  License.

  Written in Python, it can export documents to several formats
  including: HTML, XHTML, SGML, LaTeX, Lout, roff, MediaWiki, Google
  Code Wiki, DokuWiki, MoinMoin, MagicPoint, PageMaker and plain text.
- Home:     http://txt2tags.org/
- Download: http://txt2tags.org/download.html
- Usage:    Script used at build-time to generate product README as HTML page.


## Q&A 

### Question: Why Python?
Answer: Python allows remarkably fast, concise, clean and efficient designs. It
comes with many built-in features (HTTP, XML, ZIP, etc), and is platform-
independent. Not least, the initial developer (Pascal) has extensive experience
with Python.

### Question: Why WxWidgets?
Answer: WxWidgets offers a large choice of widgets, controls, containers, and is
platform-independent. The GUI features are implemented, on a given platform,
with as many native features as possible. Hence, the look and feel is the one
of the platform (unlike e.g. Java Swing). The programming model is very clean
and easy to work with. Furthermore, it has a builder, wxGlade, giving fairly
good results.

### Question: Why does the installer take up 4.6 MB?
Answer: Because it contains some parts of the Python interpreter, and
some needed libraries (e.g. WxWidgets). In fact, it will take some
more space on disk once installed.
