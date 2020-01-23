# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 06:36:57 2020

@author: fresk
"""

import numpy as np
import matplotlib.pyplot as plt

# close all figures
plt.close('all')

A0 = 4
f0 = 24
f1 = 3.375
f2 = -2.15625
Ttot = 16
N = 1024

Ts = Ttot/N
tvec = np.arange(0,np.around(N*Ts,5),Ts)
fvec = tvec/N

u = A0*np.sin(2*np.pi*f0*tvec)+0.5*A0*np.sin(2*np.pi*(f0+f1)*tvec)+0.5*A0*np.sin(2*np.pi*(f0+f2)*tvec)
U = abs(np.fft.ifft(u))

plt.figure(1)
plt.subplot(211)
plt.plot(tvec,u)
plt.xlabel('Frequentie (Hz)')
plt.ylabel('Amplitude')

plt.subplot(212)
plt.stem(fvec,U)
plt.xlabel('Frequentie (Hz)')
plt.ylabel('Magnitude')