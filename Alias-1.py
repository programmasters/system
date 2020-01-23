import numpy as np
import matplotlib.pyplot as plt

A = 1
f1 = 1
f2 = 9
t = 1
N1 = 10
N2 = 1000

T1 = 1/f1
T2 = 1/f2

Ts1 = t/N1
tijdsAs = np.arange(0,t,Ts1)

y1 = A*np.sin(2*np.pi*f1*tijdsAs)
y2 = A*np.sin(2*np.pi*f2*tijdsAs)

Ts2 = t/N2
tijdsAs1 = np.arange(0,t,Ts2)

Y1 = A*np.sin(2*np.pi*f1*tijdsAs1)
Y2 = A*np.sin(2*np.pi*f2*tijdsAs1)

plt.figure(1)
plt.subplot(311)
plt.plot(tijdsAs,y1,'ro')
plt.plot(tijdsAs1,Y1)
plt.xlabel('Time (s)')
plt.ylabel('y (m)')
plt.ylim(2,-2)
plt.subplot(312)
plt.plot(tijdsAs,y1,'ro')
plt.plot(tijdsAs,y2,'b*')
plt.xlabel('Time (s)')
plt.ylabel('y (m)')
plt.ylim(2,-2)
plt.subplot(313)
plt.plot(tijdsAs,y2,'ro')
plt.plot(tijdsAs1,Y2)
plt.xlabel('Time (s)')
plt.ylabel('y (m)')
plt.ylim(2,-2)
plt.show()