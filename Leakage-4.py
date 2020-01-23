import numpy as np
import matplotlib.pyplot as plt

A = 1 #m
fase = np.pi/2 #°

fs = 1000 #Hz
Ts = 1/fs #s
N = 32 #samples

Tend = np.around(N*Ts,5)
tvec = np.arange(0,Tend,Ts)
tvecc = np.arange(0,Tend,1/10000)

f_NL = 1/Tend

y = A*np.sin(2*np.pi*f_NL*tvec+fase)
yc = A*np.sin(2*np.pi*f_NL*tvecc+fase)

Y = np.fft.fft(y)/N
fvec = np.arange(0,fs,fs/N)

plt.figure(1,figsize=(15,10))
plt.subplot(2,2,1)
plt.plot(tvec,y,'ro')
plt.plot(tvecc,yc)
plt.xlabel('Time (s)')
plt.ylabel('y(t)')

plt.subplot(2,2,2)
plt.plot(fvec,np.abs(Y),'ro')
plt.xlabel('Frequentie (Hz)')
plt.ylabel('Amplitude (m)')

plt.subplot(2,2,3)
plt.plot(fvec,20*np.log10(np.abs(Y)),'ro')
plt.xlabel('Frequentie (Hz)')
plt.ylabel('Amplitude (dB)')

plt.subplot(2,2,4)
plt.plot(np.abs(Y),'ro')
plt.xlabel('DFT lijnnummer')
plt.ylabel('Amplitude lijn')