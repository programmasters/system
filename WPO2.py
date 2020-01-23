# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:05:34 2019

@author: manu_
"""

import numpy as np
import matplotlib.pyplot as plt

#Oef 1
time1 = np.arange(0,1,0.1)
time2 = np.arange(0,1,0.01)
sin1 = np.sin(2*np.pi*time1*1)
sin2 = np.sin(2*np.pi*time1*9)
sin1b = np.sin(2*np.pi*time2*1)
sin2b = np.sin(2*np.pi*time2*9)

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(time1,sin1,'bo')
plt.plot(time2,sin1b)
plt.subplot(2,1,2)
plt.plot(time1,sin2,'ro')
plt.plot(time1,sin2)
plt.plot(time2,sin2b)


#Oef 2a
time1 = np.arange(0,1,0.1)
time2 = np.arange(0,1,0.01)
sin2 = np.sin(2*np.pi*time1*2)
sin2b = np.sin(2*np.pi*time2*2)

sin4 = np.sin(2*np.pi*time1*4)
sin4b = np.sin(2*np.pi*time2*4)

sin6 = np.sin(2*np.pi*time1*6)
sin6b = np.sin(2*np.pi*time2*6)

sin8 = np.sin(2*np.pi*time1*8)
sin8b = np.sin(2*np.pi*time2*8)

plt.figure(2)
plt.subplot(2,2,1)
plt.plot(time1,sin2,'ro')
plt.plot(time1,sin2)
plt.plot(time2,sin2b)

plt.subplot(2,2,2)
plt.plot(time1,sin4,'ro')
plt.plot(time1,sin4)
plt.plot(time2,sin4b)

plt.subplot(2,2,3)
plt.plot(time1,sin6,'ro')
plt.plot(time1,sin6)
plt.plot(time2,sin6b)

plt.subplot(2,2,4)
plt.plot(time1,sin8,'ro')
plt.plot(time1,sin8)
plt.plot(time2,sin8b)


#Oef 2b
time1 = np.arange(0,1,0.1)
time2 = np.arange(0,1,0.01)
sin5 = np.sin(2*np.pi*time1*5)
sin5b = np.sin(2*np.pi*time2*5)

sin12 = np.sin(2*np.pi*time1*12)
sin12b = np.sin(2*np.pi*time2*12)

plt.figure(3)
plt.subplot(1,2,1)
plt.plot(time1,sin5,'ro')
plt.plot(time1,sin5)
plt.plot(time2,sin5b)

plt.subplot(1,2,2)
plt.plot(time1,sin12,'ro')
plt.plot(time1,sin12)
plt.plot(time2,sin12b)


#Oef 3
endtime = 2
samplefrequency = 100
sampleinterval = 1/samplefrequency
aantalsamples = endtime/sampleinterval

time3 = np.arange(0,endtime,sampleinterval)

frequency = np.arange(0,samplefrequency,(samplefrequency/aantalsamples))

sin3 = 2*np.sin(2*np.pi*time3*3)+np.sin(2*np.pi*time3*2)
sin3fft = np.abs(np.fft.fft(sin3))

plt.figure(4)
plt.plot(time3,sin3)
plt.plot(frequency,sin3fft)

