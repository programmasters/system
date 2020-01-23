import numpy as np
import matplotlib.pyplot as plt

A = 1
t = 1
N = 10
Nc = 1e3
Ts = t/N
Tsc = t/Nc

tvec = np.arange(0,t,Ts)
tvecc = np.arange(0,t,Tsc)

Freq = np.array([2,4,6,8])

plt.figure(1)
for i in range(len(Freq)):
    y = A*np.sin(2*np.pi*Freq[i]*tvec)
    yc = A*np.sin(2*np.pi*Freq[i]*tvecc)
    
    plt.subplot(2,2,i+1)
    plt.plot(tvec,y)
    plt.plot(tvecc, yc)
    plt.title(str(Freq[i]) +' Hz')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
