# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:29:35 2022

@author: 2175469R
"""


import numpy as np
import scipy.integrate as scint
import matplotlib.pyplot as plt
import cmath
    
def sumterm(n,a,t):
    term = 1/(2*n+1) - 1/(np.sqrt((2*n+1)*(2*n+1) + (a**2)/(t**2)))
    return term
    
def func(a,t,e):
    counter = 0
    iterations = 1000000000
    for n in range(iterations):
        x = sumterm(n,a,t)
        if n == 9999998:
            print('hello')
        if x < e:
#            print(n)
            break
        counter = counter + x
    maybeD = counter*2 - np.log(1/t)
    return maybeD

def method(a,b,t,e):
    """this is the bisection method itself"""
    if func(a,t,e)*func(b,t,e) >= 0:
       return False
    a_n = a
    b_n = b
    for n in range(30):
        m_n = (a_n + b_n)/2
        f_m_n = func(m_n,t,e)
        if func(a_n,t,e)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif func(b_n,t,e)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            return m_n
    return (a_n+b_n)/2
    

def f(E):
    out = 1/(1+np.exp(E/(k*temp)))
    return out
    
def fraction(E):

    a = cmath.sqrt(E**2-D**2)
        

    b = cmath.sqrt(((E+hbar*w)**2-D**2))

        
    out = (E**2+D**2+hbar*w*E)/(abs(a)*abs(b))
    return out

def int1(E):
    out = fraction(E)*(f(E)-f(E+hbar*w))
    return out

def int2(E):
    out = fraction(E)*(1-2*f(E+hbar*w))
    return out

def int3(E):
    a = cmath.sqrt(D**2-E**2)
        

    b = cmath.sqrt(((E+hbar*w)**2-D**2))

        
    out = (E**2+D**2+hbar*w*E)/(abs(a)*abs(b))
    out = fraction(E)*(1-2*f(E+hbar*w))
    return out

k = 1.38e-23
h = 6.63e-34
hbar = h/2*np.pi
Tc = 10
T = np.linspace(0.001,0.999,20)

freq = 4e9
w = freq*2*np.pi
temp = 0.4
d = []

for temp in T:
    d.append(1.83*method(0,1,temp,0.0001))

gap = [x*1.83*k*Tc/max(d) for x in d]
gap = gap[1:19]
T = T[1:19]
    


realSigma = []
imagSigma = []
count = 1

for D in gap:
    
    #if hbar*w<2*D:
    realSigma.append(2/(hbar*w)*scint.quad(int1,D,D*100)[0]+1/(hbar*w)*scint.quad(int2,D-hbar*w,-D)[0])
        
    #else:
    #    realSigma.append(2/(hbar*w)*scint.quad(int1,D,D*1000)[0])

    imagSigma.append(1/(hbar*w)*scint.quad(int3,D,max([D-hbar*w,-D]))[0])
    print(str(count))
    
    count+=1


plt.figure()
plt.scatter(T,realSigma)
plt.title('RealSigma')

plt.figure()
plt.scatter(T,imagSigma)
plt.title('Imaginary Sigma')




    
#plt.figure()
#plt.scatter(T,gap)

g1 = []
g2 = []
g3 = []


D = gap[17]

gRange = np.linspace(-D*10,D*10,10000)



for i in range(len(gRange)):
    g1.append(int1(gRange[i]))
    g2.append(int2(gRange[i]))
    g3.append(int3(gRange[i]))

g1opp = [-x for x in g1]
g1opp.reverse()

g2opp = [-x for x in g2]
g2opp.reverse()

g3opp = [-x for x in g3]
g3opp.reverse()


#plt.figure()
#plt.scatter(gRange,g1)
#plt.scatter(gRange,g1opp)
#plt.figure()
#plt.scatter(gRange,g2)
#plt.scatter(gRange,g2opp)
#plt.figure()
#plt.scatter(gRange,g3)
#plt.scatter(gRange,g3opp)
    



