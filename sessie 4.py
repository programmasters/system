#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:29:07 2019

@author: bart
"""

import numpy as np
import matplotlib.pyplot as plt
def DB(Lin):
    Log= 20*np.log10(Lin)
    return Log

f=np.arange(0,10000,0.001)
n=len(f)
w=2*np.pi*f
t=0.5

h=1/(1+1j*w*t)
h3db = 1/(1+1j)

plt.figure()
plt.semilogx(w,(DB(np.abs(h))))
plt.plot(1/t,DB(np.abs(h3db)),'ro')

plt.figure()
plt.semilogx(w,np.angle((h)))
plt.plot(1/t,(np.angle(h3db)),'ro')


#oef 2
wres=0.1
f=np.arange(0,10000,0.1)
w=2*np.pi*f
t=0.5
wn=10
eps=0.1
N=len(f)
h=(wn**2/(-w**2+2*eps*wn*1j*w+wn**2))
roots1=np.roots([1,2*eps*wn,wn**2])
roots=np.abs(roots1)
plt.figure()
plt.semilogx(w,(DB(np.abs(h))))
plt.axvline(roots[0],color='r')

plt.figure()
plt.semilogx(w,np.angle((h)))
plt.plot(roots[0],(np.angle((wn**2/(-(roots[0])**2+2*eps*wn*1j*(roots[0])+wn**2)))),'ro')

plt.figure()
for i in range(len(roots1)):
    plt.plot(np.real(roots1[i]),np.imag(roots1[i]),'xb')

fres=wres/(2*np.pi)
Ts=0.1
tvec=n*fres
tvec = np.arange(0,np.around(N*Ts,5),Ts)
Hhalf = h.copy()
Hhalf[int(np.round(N/2)):] = 0

h = 2*np.real(np.fft.ifft(Hhalf))
plt.figure()
plt.plot(tvec/1000,h)
plt.xlabel('Time (s)')
plt.ylabel('h(t)')