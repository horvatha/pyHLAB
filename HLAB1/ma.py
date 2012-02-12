#!/usr/bin/env python
# coding: utf-8

"""       RLC négypólus elemzése
"""

from __future__ import division
from __future__ import print_function

__author__ = 'Arpad Horvath'


#(DEFAULT:R=500,L=100mH,C=100nF,A=1; pp=4; rfreq=1)
#
########RLC négypólus paraméterek #
#
R = 0.5*10^3;          #500 ohm
L = 1.0*10^-1;         #100 mH
C = 1.0*10^-7;         #100 nF
A = 1
#
##################################
T = sqrt(L.*C)
omegac = 1./T
fcorner = omegac./(2.*pi)
kszi = 0.5*R.*C./T
Q = 1./(2.*kszi)
print("kszi = {kszi}, Q = {Q}".format(kszi=kszi, Q=Q))
##################################
#      FREQUENCY DOMAIN 
##################################
wmax = omegac.*10^3
d = wmax./10^5
omega  =  d:d:wmax
phc = 80./pi;                    #pi <=== 80 dB (lépték)
q = A./(1.+i*omega.*T./Q-omega.^2.*T.^2);          #transfer function
Y = 20*log10(abs(q));            #BODE amplitudó
PH = phc.*angle(q);              #BODE fázis
subplot(2,1,1);  plot(omega,Y,'k.',omega,PH,'m--')
axis([d wmax -80 20])
set(gca,'XScale','log','YScale','linear')
set(gca,'XGrid','on','YGrid','on')
set(gca,'XColor','blue','YColor','blue')
legend ('absY','\phi(\omega)')
xlabel '\omega [rad/s]'
ylabel 'absY(j\omega)  [dB]'
title 'MA BODE-jelleggörbék'

##################################################
#               TIME DOMAIN
##################################################
pp = 4;                     #kirajzolt periódusszám, rfreq=1 esetén
# Tkp. az oszcilloszkóp idõalapjának beállítása!
#
SimTime = pp./fcorner;       #simulation time [s]
N = 1000;                    #sampling point number
Ts = SimTime./N             #sampling period

#gyökök az 'S' síkon
k = Ts.*fcorner

root1 = k.*(-kszi+sqrt(kszi^2-1))
root2 = k.*(-kszi-sqrt(kszi^2-1))
B = 2.*exp(2.*pi.*real(root1))*cos(2.*pi.*imag(root1))
C = -exp(4.*pi.*real(root1))
K = 1-B-C

AM = 0
BM = 0

xb = zeros(1,N+1)
xk = zeros(1,N+1)

# A vizsgálójel paraméterei
rfreq = 10
#jelfrekvencia = törésponti frekv.*rfreq 
#a jelgenerátor vizsgálójelének frekvenciája.
####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
samp = 1;         %csúcsérték amplitudója  [V]
%
 t = 1:1:N+1
%%%%%%%%%%%%%%%%  bemenõjel típus választás! %%%%%%%
%négyszög
xb(1,t) = samp.*sign(sin((t-1).*rfreq.*pp.*2.*pi./(N)))
%xb(1,t) = samp.*sin((t-1).*rfreq.*pp.*2.*pi./(N))
%szinuszos
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for t = 1:1:N+1
    xk(1,t) = K.*A.*xb(1,t)+B.*AM+C.*BM
    BM = AM
    AM = xk(1,t)
end
L = 1:1:N+1
subplot(2,1,2);  plot(L,xb,'m',L,xk,'k')
gmx = samp.*3
gmin = -gmx

axis([1 N+1 gmin gmx])
set(gca,'XScale','linear','YScale','linear')
set(gca,'XGrid','on','YGrid','on')
set(gca,'XColor','blue','YColor','blue')
legend ('in','out')
xlabel 't: *Ts  [s]'
xlabel 'u  [V]'
title 'MA jelátvitel'

