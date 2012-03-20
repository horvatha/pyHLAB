#!/usr/bin/env python
# coding: utf-8

"""       RLC négypólus elemzése
"""

from __future__ import division
from __future__ import print_function
from pylab import *

__author__ = 'Arpad Horvath'


#(DEFAULT:R=500,L=100mH,C=100nF,A=1; pp=4; rfreq=1)
#
########RLC négypólus paraméterek #
#
R = 0.5e3;          #500 ohm
L = 1.0e-1;         #100 mH
C = 1.0e-7;         #100 nF
A = 1
#
##################################
T = sqrt(L*C)
omegac = 1/T
fcorner = omegac/(2*pi)
xi = 0.5*R*C/T
Q = 1/(2*xi)
print("xi = {xi}, Q = {Q}".format(xi=xi, Q=Q))
##################################
#      FREQUENCY DOMAIN 
##################################
wmax = omegac*1e3
d = wmax/1e5
omega  =  arange(d,wmax,d)
phc = 80/pi                    #pi <=== 80 dB (lépték)
q = A/(1.+1j*omega*T/Q-omega**2*T**2)          #transfer function
Y = 20*log10(abs(q))            #BODE amplitudó
PH = phc*angle(q)              #BODE fázis
subplot(2,1,1)
semilogx(omega,Y,'k.',omega,PH,'m--')
axis([d,wmax,-80,20])
grid(True)
legend(['absY','\phi(\omega)'])
xlabel('\omega [rad/s]')
ylabel('absY(j\omega)  [dB]')
title('MA BODE-jelleggörbék')

##################################################
#               TIME DOMAIN
##################################################
pp = 4    #kirajzolt periódusszám, rfreq=1 esetén
# Tkp. az oszcilloszkóp időalapjának beállítása!
#
SimTime = pp/fcorner       #simulation time [s]
N = 1000                   #sampling point number
Ts = SimTime/N             #sampling period

#gyökök az 'S' síkon
k = Ts*fcorner

root1 = k*(-xi+sqrt(xi**2-1))
root2 = k*(-xi-sqrt(xi**2-1))
B = 2*exp(2*pi*real(root1))*cos(2*pi*imag(root1))
C = -exp(4*pi*real(root1))
K = 1-B-C

AM = 0
BM = 0

xb = zeros(N+1)
xk = zeros(N+1)

# A vizsgálójel paraméterei
rfreq = 10
#jelfrekvencia = törésponti frekv*rfreq
#a jelgenerátor vizsgálójelének frekvenciája.
########################################################
samp = 1         #csúcsérték amplitudója  [V]

t = arange(N+1)
################  bemenőjel típus választás! #######
#négyszög
xb = samp*sign(sin((t-1)*rfreq*pp*2*pi/(N)))
#xb = samp*sin((t-1)*rfreq*pp*2*pi/(N))
#szinuszos
####################################################
for t in range(N+1):
    xk = K*A*xb+B*AM+C*BM
    BM = AM
    AM = xk
L = arange(N+1)
subplot(2,1,2)
plot(L,xb,'m',L,xk,'k')
gmx = samp*3
gmin = -gmx

axis([1,N+1,gmin,gmx])
grid(True)
legend(['in','out'])
xlabel('t: *Ts  [s]')
xlabel('u  [V]')
title('MA jelátvitel')

