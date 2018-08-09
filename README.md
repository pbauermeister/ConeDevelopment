# ConeDevelopment

(C) by Pascal Bauermeister, 2018.

## A. Purpose

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

This program was inspired by an interesting discussion I had with Udo
Bund, my wife's uncle. It was about the construction of a cap to fit
on the nozzle of a high-pressure Kärcher cleaner in order to reduce
the lateral projections.

## B. Building process

The build process for Debian Linux, Mac OSX and Microsoft Windows has not been (re)tested. Please be patient.

## C. How to run?

Binary distributions (install packages) will be made available (as soon as the build process is working).

Meanwhile you can install Python and needed libraries, and run from the command-line:
```
git clone https://github.com/pbauermeister/ConeDevelopment.git
cd ConeDevelopment
python conedevelopment.py
```

## D. Copyright, licenses and credits

See [copyright, license and credits](https://github.com/pbauermeister/ConeDevelopment/blob/master/COPYRIGHT_LICENSE_CREDITS.md).
