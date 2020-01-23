import numpy as np
import matplotlib.pyplot as plt

f = 2 #Hz
fs = 10 #Hz
fc = 1e3 #Hz
t = 1 # s

Ts = t/fs
Tc = t/fc

N = np.array([10,11,12,13,14,15])
k = len(N)

for A in range(k):
    
    T = N[A]*Ts
    tvec = np.arange(0,np.around(T,3),Ts)
    tvecc = np.arange(0,T,Tc)
    y = np.sin(2*np.pi*f*tvec)
    yc = np.sin(2*np.pi*f*tvecc)
    
    Y = np.fft.fft(y)/N[A]
    fvec = np.arange(0,fs,fs/N[A])
    
    
    plt.figure(A+1,figsize=(10,5))
    plt.subplot(1,2,1)
    plt.plot(tvec,y,'ro')
    plt.plot(tvecc,yc)
    plt.xlabel('Time (s)')
    plt.ylabel('y(t)')
    plt.subplot(1,2,2)
    plt.stem(fvec,np.abs(Y))
    plt.xlabel('Frequentie (Hz)')
    plt.ylabel('Y')
