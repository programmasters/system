#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 19:05:13 2020

@author: bart
"""




import numpy as np
import matplotlib.pyplot as plt

# close all figures
plt.close('all')

def db(x):
    x = 20*np.log10(np.abs(x)) #p74 theorie: amplitude in dB
    return x


# 4.1: eerste orde systeem
tau = 0.5
wvec = np.arange(0,100,0.01)
N = len(wvec)

H = 1/(1+1j*wvec*tau)

H3db = 1/(1+1j)

plt.figure(1)
plt.subplot(211)
plt.semilogx(wvec,db(H))
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Amplitude (dB)')
plt.plot(1/tau,db(H3db), 'ro')

plt.subplot(212)
plt.semilogx(wvec,np.angle(H))
plt.plot(1/tau,np.angle(H3db), 'ro')
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Amplitude (dB)')


#♦ 4.2: Tweede orde systeem

wn = 10
ksi = 0.1


wvec = np.arange(0,1000,0.1)
N = len(wvec)

H = wn**2/(-wvec**2+2*ksi*wn*1j*wvec+wn**2)

p1 = -ksi*wn+wn*np.sqrt(complex(ksi**2-1)) #to avoid nan for sqrt 0
p2 = -ksi*wn-wn*np.sqrt(complex(ksi**2-1))

plt.figure(2)
plt.subplot(211)
plt.semilogx(wvec,db(H))
plt.plot([np.imag(p1),np.imag(p1)],[-100,20],'r') #rode lijn, ligt op
#imaginaire pool
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Amplitude (dB)')


plt.subplot(212)
plt.semilogx(wvec,np.angle(H))
plt.plot(np.imag(p1),-np.pi/2, 'ro')
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Fase (rad)')

plt.figure(3)
plt.plot(np.real(p1),np.imag(p1), 'bx')
plt.plot(np.real(p2),np.imag(p2),'bx')
plt.plot([-10,5],[0,0], 'k-')
plt.plot([0,0],[-15,15], 'k-')
plt.xlim(-10,5)
plt.ylim(-15,15)

# impuls response
wRes =  wvec[1]-wvec[0]
fRes =  wRes/(2*np.pi)
fs = fRes*N
Ts = 1/fs

tvec = np.arange(0,np.around(N*Ts,5),Ts)

Hhalf = H.copy()
Hhalf[int(np.round(N/2)):] = 0

h = 2*np.real(np.fft.ifft(Hhalf))
plt.figure(4)
plt.plot(tvec,h)
plt.xlabel('Time (s)')
plt.ylabel('h(t)')


# 4.3.1: FRF op basis van nullen en polen

p1 = 0.1+5*1j
p2 = 0.1-5*1j
p3 = -3

n1 = -2

wRes = 0.1

wvec = np.arange(0, 100, wRes)
N = len(wvec)

s = 1j*wvec
H = (s-n1)/((s-p1)*(s-p2)*(s-p3))
#H = 1/((s-p1)*(s-p2))


plt.figure(5)
plt.subplot(211)
plt.semilogx(wvec,db(H))
plt.xlabel('Angular Frecuency (rad/s)')
plt.ylabel('Amplitude (dB)')
plt.subplot(212)
plt.semilogx(wvec,np.angle(H))
plt.xlabel('Angular Frecuency (rad/s)')
plt.ylabel('Fase (rad)')

plt.figure(6)
plt.plot(np.real(p1),np.imag(p1),'bx')
plt.plot(np.real(p2),np.imag(p2),'bx')
plt.plot(np.real(p3),np.imag(p3),'bx')
plt.plot(np.real(n1),np.imag(n1),'bo')
plt.plot([-10,5],[0,0],'k-')
plt.plot([0,0],[-10,10],'k-')
plt.xlim(-10,5)
plt.ylim(-10,10)

fRes = wRes/(2*np.pi)
fs = fRes*N
Ts = 1/fs

tvec = np.arange(0,np.around(N*Ts,5),Ts)

Hhalf = H.copy()
Hhalf[int(np.round(N/2)):] = 0

h = 2*np.real(np.fft.ifft(Hhalf))
plt.figure(7)
plt.plot(tvec,h)
plt.xlabel('Time (s)')
plt.ylabel('h(t)')

# 4.3.2: plot polen nullen map

# num = 10s^2 + 50s +3
# denom = s^3 + 6s^2 + 630.2s + 3125

nullen = np.roots([10, 50, 3])
polen = np.roots([1, 6, 630.2, 3125])

plt.figure(8)
for n in range(len(nullen)):
    plt.plot(np.real(nullen[n]),np.imag(nullen[n]),'bo')

for p in range(len(polen)):
    plt.plot(np.real(polen[p]),np.imag(polen[p]),'bx')
    
plt.plot([-6,2],[0,0],'k-')
plt.plot([0,0],[-30,30],'k-')
plt.xlim(-6,2)
plt.ylim(-30,30)

# 4.4: Simuleren van een output


fs = 100 #geldt voor signaal en voor TF (discreet systeem functie v)
Ts = 1/fs
N = 3000
f = 2

tvec = np.arange(0,np.around(N*Ts,5),Ts)
u = np.sin(2*np.pi*f*tvec)

fvec = np.arange(0,fs,fs/N)
wvec = fvec*2*np.pi

wn = 10
ksi = 0.1

# 4.4.1: Frequentiedomein
H = wn**2/(-wvec**2+2*ksi*wn*1j*wvec+wn**2)
U = np.fft.fft(u)/N
Y = np.multiply(H,U) #output scaled by N since U was scaled by N

plt.figure(9)
plt.stem(fvec,np.abs(Y), 'r')
plt.stem(fvec,np.abs(U), 'b')
plt.xlabel('Frequentie (Hz)')
plt.ylabel('|Y|')
plt.xlim([0, 10])


# 4.4.2: Tijdsdomein
Hhalf = H.copy()
Hhalf[int(np.round(N/2)):] = 0

h = 2*np.real(np.fft.ifft(Hhalf))

y = np.convolve(h,u)

plt.figure(10)
plt.plot(tvec,u,'b')
plt.plot(tvec,y[0:N],'r')
plt.xlabel('Time (s)')
plt.ylabel('y(t)')