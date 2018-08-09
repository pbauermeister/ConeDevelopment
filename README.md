# ConeDevelopment

(C) by Pascal Bauermeister, 2018.

## Purpose

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

![Screenshot](/Screenshot.png)

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

## History 

- 2018-08-09 Initial release


## How to Get the Sources

See https://github.com/pbauermeister/ConeDevelopment

## Copyright, licenses and credits

See [copyright, license and credits](https://github.com/pbauermeister/ConeDevelopment/blob/master/COPYRIGHT_LICENSE_CREDITS.md).

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
