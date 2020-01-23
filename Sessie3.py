#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 08:09:59 2019

@author: bart
"""
import numpy as np
import matplotlib.pyplot as plt

xt=np.arange(-1,3.1,0.1)
yt=np.sin(2*np.pi*xt*2)
y=yt[0:10]
x=xt[0:10]

FR=np.abs(np.fft.fft(y))  
fr=np.abs(np.fft.fftshift(y))
plt.figure(1)
plt.plot(xt,yt)
plt.plot(x,y,'ro')
plt.show()
plt.figure(2)
z=np.arange(0,10,10/10)
plt.stem(z,FR)
plt.show()

xt=np.arange(-1,3.1,0.1)
yt=np.sin(2*np.pi*xt*2)
y=yt[0:12]
x=xt[0:12]

FR=np.abs(np.fft.fft(y))  
fr=np.abs(np.fft.fftshift(y))
plt.figure(3)
plt.plot(xt,yt)
plt.plot(x,y,'ro')
plt.show()
plt.figure(4)
z=np.arange(0,10,10/12)
plt.stem(z,FR)
plt.show()

xt=np.arange(-1,3.1,0.1)
yt=np.sin(2*np.pi*xt*2)
y=yt[0:15]
x=xt[0:15]

FR=np.abs(np.fft.fft(y))  
fr=np.abs(np.fft.fftshift(y))
plt.figure(5)
plt.plot(xt,yt)
plt.plot(x,y,'ro')
plt.show()
plt.figure(6)
z=np.arange(0,10,10/15)
plt.stem(z,FR)
plt.show()

#oef 2
xt=np.arange(0,0.0150,0.001)
yt=np.sin((2*np.pi*80*xt)+(np.pi/2))
plt.figure(1)
plt.plot(xt,yt)

FR=np.abs(np.fft.fft(yt))  
plt.figure(2)
z=np.arange(0,1000,1000/15)
plt.plot(z,FR,'bx')

FR=np.abs(np.fft.fft(yt))  
plt.figure(3)
z=np.arange(0,1000,1000/15)
FR=FR/16
plt.figure(3)
plt.plot(FR,'bx')
plt.figure(4)
plt.plot(z,FR,'bx')

#nu in decibel

xt=np.arange(0,0.0150,0.001)
yt=np.sin((2*np.pi*80*xt)+(np.pi/2))
FR=20*np.log10(yt)

plt.plot(xt,yt)

FR=np.abs(np.fft.fft(yt))  
plt.figure(2)
z=np.arange(0,1000,1000/15)
FR=20*np.log10(FR)
z=np.log10(z)
plt.plot(z,FR,'bx')

FR=np.abs(np.fft.fft(yt))  
plt.figure(3)
z=np.arange(0,1000,1000/15)
FR=20*np.log10(FR)

plt.figure(3)
plt.plot(FR,'bx')
plt.figure(4)
plt.plot(z,FR,'bx')








#oef 3
#operiode moet perfect met window overeen komen
N = 16
Ts =0.001
xt=np.arange(0,N*Ts,Ts)
yt=np.sin((2*np.pi*1/(N*Ts))*xt+(np.pi/2))
plt.figure(1)
plt.plot(xt,yt)

FR=np.abs(np.fft.fft(yt))  
plt.figure(2)
z=np.arange(0,1000,1000/N)
FR=20*np.log10(FR)
plt.plot(z,FR,'bx')

FR=np.abs(np.fft.fft(yt))  
plt.figure(3)
z=np.arange(0,1000,1000/N)
FR=FR/N
#bovensaande is om de amplitude te corrigeren



plt.plot(FR,'bx')
plt.show
plt.plot(z,FR,'bx')
plt.show

#oef 4
#operiode moet perfect met window overeen komen
N = 32
Ts =0.001
xt=np.arange(0,N*Ts,Ts)
yt=np.sin((2*np.pi*1/(N*Ts))*xt+(np.pi/2))
plt.figure(1)
plt.plot(xt,yt)

FR=np.abs(np.fft.fft(yt))  
plt.figure(2)
z=np.arange(0,1000,1000/N)
FR=20*np.log10(FR)
plt.plot(z,FR,'bx')

FR=np.abs(np.fft.fft(yt))  
plt.figure(3)
z=np.arange(0,1000,1000/N)
FR=FR/N
#bovensaande is om de amplitude te corrigeren


plt.figure(3)
plt.plot(FR,'bx')
plt.figure(4)
plt.plot(z,FR,'bx')



#oef 6
#operiode moet perfect met window overeen komen
N = 1023
Ts =1/1024
f=1024
f1=20.5
f2=200.5
xt=np.arange(0,N*Ts,Ts)
yt=np.sin(2*np.pi*f1*xt)+(10**-4)*np.sin((2*np.pi*f2*xt))
plt.figure(1)
plt.plot(xt,yt)

FR=np.abs(np.fft.fft(yt))  
plt.figure(2)
z=np.arange(0,f,f/N)
FR=20*np.log10(FR)
plt.plot(z,FR,'b.')
plt.xlim(0,500)

