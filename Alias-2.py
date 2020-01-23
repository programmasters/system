import numpy as np
import matplotlib.pyplot as plt

A = 1

f1 = 2
f2 = 4
f3 = 6
f4 = 8
f5 = 5
f6 = 12

t = 1
N1 = 10
N2 = 1000

T1 = 1/f1
T2 = 1/f2
T3 = 1/f3
T4 = 1/f4
T5 = 1/f5
T6 = 1/f6

Ts1 = t/N1
tijdsAs = np.arange(0,t,Ts1)

y1 = A*np.sin(2*np.pi*f1*tijdsAs)
y2 = A*np.sin(2*np.pi*f2*tijdsAs)
y3 = A*np.sin(2*np.pi*f3*tijdsAs)
y4 = A*np.sin(2*np.pi*f4*tijdsAs)
y5 = A*np.sin(2*np.pi*f5*tijdsAs)
y6 = A*np.sin(2*np.pi*f6*tijdsAs)


Ts2 = t/N2
tijdsAs1 = np.arange(0,t,Ts2)

Y1 = A*np.sin(2*np.pi*f1*tijdsAs1)
Y2 = A*np.sin(2*np.pi*f2*tijdsAs1)
Y3 = A*np.sin(2*np.pi*f3*tijdsAs1)
Y4 = A*np.sin(2*np.pi*f4*tijdsAs1)
Y5 = A*np.sin(2*np.pi*f5*tijdsAs1)
Y6 = A*np.sin(2*np.pi*f6*tijdsAs1)


plt.figure(1,figsize=(9,5))
plt.subplot(121)
plt.plot(tijdsAs,y1,'ro')
plt.plot(tijdsAs1,Y1)
plt.xlabel('Time (s)')
plt.ylabel('y (m)')
plt.title('2Hz')
plt.ylim(-1.1,1.1)

plt.subplot(122)
plt.plot(tijdsAs,y2,'ro')
plt.plot(tijdsAs1,Y2)
plt.xlabel('Time (s)')
plt.ylabel('y (m)')
plt.title('4Hz')
plt.ylim(-1.1,1.1)

plt.figure(2, figsize=(9,5))
plt.subplot(121)
plt.plot(tijdsAs,y3,'ro')
plt.plot(tijdsAs1,Y3)
plt.xlabel('Time (s)')
plt.ylabel('y (m)')
plt.title('6 Hz')
plt.ylim(-1.1,1.1)

plt.subplot(122)
plt.plot(tijdsAs,y4,'ro')
plt.plot(tijdsAs1,Y4)
plt.xlabel('Time (s)')
plt.ylabel('y (m)')
plt.title('8 Hz')
plt.ylim(-1.1,1.1)

plt.figure(3, figsize=(9,5))
plt.subplot(121)
plt.plot(tijdsAs,y5,'ro')
plt.plot(tijdsAs1,Y5)
plt.xlabel('Time (s)')
plt.ylabel('y (m)')
plt.title('5 Hz')
plt.ylim(-1.1,1.1)

plt.subplot(122)
plt.plot(tijdsAs,y6,'ro')
plt.plot(tijdsAs1,Y6)
plt.xlabel('Time (s)')
plt.ylabel('y (m)')
plt.title('12 Hz')
plt.ylim(-1.1,1.1)

plt.show()