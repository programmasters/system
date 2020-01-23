import numpy as np
import matplotlib.pyplot as plt

f1 = 20.5 #Hz
f2 = 200.5 #Hz

Ts = 1/1024
fs = 1/Ts
N = 1024

#Rechthoekig venster

tvec = np.arange(0,np.around(N*Ts,5),Ts)
fvec = np.arange(0,fs,fs/N)

y = np.sin(2*np.pi*f1*tvec)+10e-4*np.sin(2*np.pi*f2*tvec)
Y = np.fft.fft(y)/N

plt.figure(1,figsize=(15,10))
plt.subplot(2,2,1)
plt.plot(tvec,y)
plt.xlabel('Time (s)')
plt.ylabel('y(t)')

plt.subplot(2,2,2)
plt.plot(fvec,20*np.log10(np.abs(Y)))
plt.xlabel('Frequentie (Hz)')
plt.ylabel('Amplitude (dB)')

#Venster van Hann

window = np.hanning(N)
yh = np.multiply(y,window)
Yh = np.fft.fft(yh)

plt.figure(1,figsize=(15,10))
plt.subplot(2,2,3)
plt.plot(tvec,yh)
plt.xlabel('Time (s)')
plt.ylabel('y(t)')

plt.subplot(2,2,4)
plt.plot(fvec,20*np.log10(np.abs(Yh)))
plt.xlabel('Frequentie (Hz)')
plt.ylabel('Amplitude (dB)')