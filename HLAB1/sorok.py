#!/usr/bin/env python
# coding: utf-8

"""Fourier-sorok közelítő összegei
"""


import pylab
from pylab import sin, pi, plot

tagok = {
    "fűrészfog" : lambda i, x: 2/pi/i*sin(i*x),
    "négyszög" : lambda i, x: 4/pi/i*sin(i*x) if i%2 == 1 else 0,
    "háromszög" : lambda i, x: 8/pi**2*(-1)**((i-1)/2)/i**2*sin(i*x) if i%2 == 1 else 0,
}

def sor_abra(tipus=None, nn=None):
    """Kirajzolja különböző Fourier-sorok közelítő összegeit.

    Paraméterek:
        tipus: sztring
            lehet  1: "fűrészfog" 2: "négyszög" vagy 3: "háromszög"
        nn: lista
            hányadik közelítő összegeket rajzolja

    """

    if isinstance(tipus, int):
        tipus = ["fűrészfog", "négyszög", "háromszög"][tipus-1]
    if tipus not in tagok:
        tipus = "háromszög"
    if nn is None:
        nn = [1, 5, 10, 50]

    x=pylab.linspace(-pi, 3*pi, 1000)
    for n in nn:
        y=pylab.zeros(1000)
        for i in range(1,n+1):
            y+=tagok[tipus](i,x)
        if n == nn[-1]:
            plot(x,y, "-k", hold=True, label="n=%d"%n)
        else:
            plot(x,y, ":", hold=True, label="n=%d"%n)
    pylab.legend(loc="lower right")
    pylab.title(tipus.decode("utf-8"))
