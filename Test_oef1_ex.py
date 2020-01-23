# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 10:34:11 2020

@author: fresk
"""

import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

def db(x):
    x = 20*np.log10(np.abs(x))
    return x

K1 = 64
K2 = 1445
p1 = -0.72+7.97*1j
p2 = -0.72-7.97*1j
a = 1
b = 6
c = 296
d = 1445

wvec = np.arange(0,1000,0.1)
N = len(wvec)

s = 1j*wvec

H1 = K1/((s-p1)*(s-p2))
H2 = K2/(a*s**3+b*s**2+c*s+d)
H = H1*H2
A = np.abs(H)
fase = np.angle(H)
radialen = np.unwrap(fase)


res1 = np.abs(p1)
poles = np.roots([a, b, c, d])
res2 = np.abs(poles[0])
br1 = np.abs(poles[2])

plt.figure(1)
plt.subplot(211)
plt.semilogx(wvec,db(H))
plt.plot([res1, res1], [20,-200], 'r')
plt.plot([res2, res2], [20,-200], 'r')
plt.plot([br1, br1], [20,-200], 'g')
plt.xlabel('Frequentie (rad/s)')
plt.ylabel('Amplitude (dB)')

plt.subplot(212)
plt.semilogx(wvec,(np.unwrap(fase)*(180/np.pi)))
plt.plot([res1, res1], [0,-450], 'r')
plt.plot([res2, res2], [0,-450], 'r')
plt.plot([br1, br1], [0,-450], 'g')
plt.xlabel('Frequentie (rad/s)')
plt.ylabel('Fase (deg)')


