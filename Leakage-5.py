import numpy as np
import matplotlib.pyplot as plt

A = 1 #m
phi = np.pi/2 #°
N3 = 16 # aantal samples
N5 = 32 # aantal samples
fs3 = 1000 #Hz


Tend = np.around(N3*(1/fs3),5)
Ts = Tend/N5
fs = 1/Ts


f_NL = 1/(Ts*N5)

tvec = np.arange(0,Tend,Ts)
tvecc = np.arange(0,Tend,1/10000)

y = A*np.sin(2*np.pi*f_NL*tvec+phi)
yc = A*np.sin(2*np.pi*f_NL*tvecc+phi)

Y = np.fft.fft(y)/N5

fvec = np.arange(0,fs,fs/N5)


plt.figure(1,figsize=(15,10))
plt.subplot(2,2,1)
plt.plot(tvec,y,'ro')
plt.plot(tvecc,yc)
plt.xlabel('Time (s)')
plt.ylabel('y(t)')

plt.subplot(2,2,2)
plt.plot(fvec,20*np.log10(np.abs(Y)),'ro')
plt.xlabel('Frequentie (Hz)')
plt.ylabel('Amplitude (dB)')

plt.subplot(2,2,3)
plt.plot(np.abs(Y),'ro')
plt.xlabel('DFT lijnnummer')
plt.ylabel('Amplitude lijn')

plt.subplot(2,2,4)
plt.plot(fvec,np.abs(Y),'ro')
plt.xlabel('Frequentie (Hz)')
plt.ylabel('Amplitude lijn')