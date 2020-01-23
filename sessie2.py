#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:06:54 2019

@author: bart
"""
import numpy as np
import matplotlib.pyplot as plt

# sini met lage sampling rate

T=np.arange(0,1,0.1)
f1=np.sin(2*np.pi*T*1)
f2=np.sin(2*np.pi*T*9)
plt.figure(1)
plt.plot (T,f1,'bo')
plt.plot (T,f2,'ro')
plt.show

#zelfde sini met hogere sampling rate


T=np.arange(0,1,0.01)
f1=np.sin(2*np.pi*T*1)
f2=np.sin(2*np.pi*T*9)
plt.figure(1)
plt.plot (T,f1)
plt.plot (T,f2)
plt.show

T=np.arange(0,1,0.1)
f1=np.sin(2*np.pi*T*2)
f2=np.sin(2*np.pi*T*4)
f3=np.sin(2*np.pi*T*6)
f4=np.sin(2*np.pi*T*8)


T1=np.arange(0,1,0.001)
hf1=np.sin(2*np.pi*T1*2)
hf2=np.sin(2*np.pi*T1*4)
hf3=np.sin(2*np.pi*T1*6)
hf4=np.sin(2*np.pi*T1*8)

plt.figure(1)
plt.subplot(2,2,1)
plt.plot (T,f1)
plt.plot (T1,hf1)
plt.subplot(2,2,2)
plt.plot (T,f2)
plt.plot (T1,hf2)
plt.subplot(2,2,3)
plt.plot (T,f3)
plt.plot (T1,hf3)
plt.subplot(2,2,4)
plt.plot (T,f4)
plt.plot (T1,hf4)
plt.show

T=np.arange(0,1,0.1)
f1=np.sin(2*np.pi*T*5)
f2=np.sin(2*np.pi*T*12)

T1=np.arange(0,1,0.001)
hf1=np.sin(2*np.pi*T1*5)
hf2=np.sin(2*np.pi*T1*12)

plt.figure(2)
plt.subplot(1,2,1)
plt.plot (T,f1)
plt.plot (T1,hf1)
plt.subplot(1,2,2)
plt.plot (T,f2)
plt.plot (T1,hf2)
plt.show

#oef3


x=np.arange(0,2,0.01)
y=np.sin(2*np.pi*x*3)

FR=np.abs(np.fft.fft(y))  
fr=np.fft.fftshift(FR)
plt.figure(3)
plt.plot(x,y)

z=np.arange(-50,50,0.5)
plt.plot(z,fr)
plt.show()