#!/usr/bin/env python
# coding: utf-8
from __future__ import division
__author__ = "Horváth Árpád, 2009"
# A mozgóképet az alábbi parancs hozta létre (ImageMagick):
# convert -delay 100 -loop 0 *.png fourier.gif

import pylab
from pylab import show, plot, linspace
from pylab import zeros
from pylab import sin, pi

def fourier(n=15, save=False):
    x = pylab.linspace(-4.8, 4.8, 1024)
    y = pylab.zeros(1024)
    pylab.grid(False)
    pylab.hold(False)
    for i in range(1,n+1,2):
        y += sin(i*x)/i
    pylab.plot(x,4/pi*y, "b")
    pylab.title(u"Négyszögjel Fourier-sora, %d tag" %n)
    if save:
        pylab.savefig("fourier%02d.png" % n)
    pylab.show()

if __name__ == "__main__":
    for i in range(1,33,2):
        fourier(i, save=True)
