# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

L = ['A',0,'B'];
print (L[1]);

A=np.array([11,2,30])
B=np.zeros((3,3))
C=np.arange(1,100)
print('grootte van array B is ' + str(np.shape(B)))

Dict = {
        'L':L,
        'A':A,
        'getal':3
        }

X=np.arange(0,1,0.02)
Y=np.exp(-0.8*X)
    
  
def vrijeVal(Z0,t):
    z= Z0-(((9.81*t**2))/2)
    return z


T=np.arange(0,5,0.1)
ztest = vrijeVal(4,T)
print (ztest)


plt.figure(1)
plt.plot (X,Y)
plt.xlabel('X')
plt.ylabel('Y')
plt.show

T=np.arange(0,3,0.01)
Lijn1=vrijeVal(100,T)
Lijn2=vrijeVal(75,T)


plt.figure(2)
plt.subplot(2,1,1)
plt.plot (T,Lijn1)
plt.xlabel('X')
plt.ylabel('Y')
plt.subplot(2,1,2)
plt.plot (T,Lijn2)
plt.xlabel('X')
plt.ylabel('Y')
plt.show
T=np.arange(0,0.51,0.0051)
Y=2*np.sin(2*np.pi*4*T)

plt.figure(3)
plt.plot (T,Y)
plt.xlabel('T')
plt.ylabel('Y')
plt.show
T=np.arange(0,0.51,0.051)
Y2=2*np.sin(2*np.pi*4*T)

plt.plot (T,Y2)

T=np.arange(0,1,0.005)
Y3=np.sin(2*np.pi*T)

plt.figure(4)
plt.plot (T,Y3)
plt.show


Y4=np.concatenate((Y3,Y3),axis=None)
T2=np.concatenate((T,1+T),axis=None)

plt.figure(5)
plt.plot (T2,Y4)
plt.show


T=np.arange(0,0.8,0.001)
Y1=20*np.sin(2*np.pi*5*T)+4*np.sin(2*np.pi*15*T)

plt.figure(6)
plt.plot (T,Y1)

plt.show



for i in range(len(L)):
  print(L[i])
  
  
X=np.arange(-2,2,0.01)
Y1=4-X**2
plt.figure(7)
plt.plot (X,Y1)
plt.show
Y=8/3
for k in range(1,200) :
    Y=Y+((16/(k*np.pi)**2))*((-1)**(k+1))*np.cos(k*np.pi*X/2)
    
plt.figure(8)
plt.plot (X,Y)
plt.show

