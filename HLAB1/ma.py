#!/usr/bin/env python
# coding: utf-8

"""       RLC n�gyp�lus elemz�se
"""

from __future__ import division
from __future__ import print_function

__author__ = 'Arpad Horvath'


#(DEFAULT:R=500,L=100mH,C=100nF,A=1; pp=4; rfreq=1)
#
########RLC n�gyp�lus param�terek #
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
phc = 80./pi;                    #pi <=== 80 dB (l�pt�k)
q = A./(1.+i*omega.*T./Q-omega.^2.*T.^2);          #transfer function
Y = 20*log10(abs(q));            #BODE amplitud�
PH = phc.*angle(q);              #BODE f�zis
subplot(2,1,1);  plot(omega,Y,'k.',omega,PH,'m--')
axis([d wmax -80 20])
set(gca,'XScale','log','YScale','linear')
set(gca,'XGrid','on','YGrid','on')
set(gca,'XColor','blue','YColor','blue')
legend ('absY','\phi(\omega)')
xlabel '\omega [rad/s]'
ylabel 'absY(j\omega)  [dB]'
title 'MA BODE-jellegg�rb�k'

##################################################
#               TIME DOMAIN
##################################################
pp = 4;                     #kirajzolt peri�dussz�m, rfreq=1 eset�n
# Tkp. az oszcilloszk�p id�alapj�nak be�ll�t�sa!
#
SimTime = pp./fcorner;       #simulation time [s]
N = 1000;                    #sampling point number
Ts = SimTime./N             #sampling period

#gy�k�k az 'S' s�kon
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

# A vizsg�l�jel param�terei
rfreq = 10
#jelfrekvencia = t�r�sponti frekv.*rfreq 
#a jelgener�tor vizsg�l�jel�nek frekvenci�ja.
####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
samp = 1;         %cs�cs�rt�k amplitud�ja  [V]
%
 t = 1:1:N+1
%%%%%%%%%%%%%%%%  bemen�jel t�pus v�laszt�s! %%%%%%%
%n�gysz�g
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
title 'MA jel�tvitel'

