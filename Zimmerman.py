# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:23:41 2022

@author: 2175469R
"""

import numpy as np
import scipy.integrate as scint
import matplotlib.pyplot as plt

def integral1(E,w):
    P1 = np.sqrt((E+w)**2-D**2)
    P2 = np.sqrt((E**2-D**2))
    P3 = np.sqrt((E-w)**2-D**2)
    P4 = 1j*np.sqrt(D**2-(E-w)**2)
    
    I1 = np.tanh(E/(2*k*T)*(((1-(D**2+E*(E-w))/P4*P2))*1/(P4+P2+1j/tau)-((1+(D**2+E*(E-w))/P4*P2))*1/(P4-P2+1j/tau)))

    return I1


def integral2(E,w):
    P1 = np.sqrt((E+w)**2-D**2)
    P2 = np.sqrt((E**2-D**2))
    P3 = np.sqrt((E-w)**2-D**2)
    P4 = 1j*np.sqrt(D**2-(E-w)**2)

    I2 = np.tanh((E+w)/(2*k*T)*(((1-(D**2+E*(E+w))/P1*P2))*1/(P1-P2+1j/tau)-((1+(D**2+E*(E+w))/P1*P2))*1/(-P1-P2+1j/tau))) \
    +np.tanh(E/(2*k*T)*(((1+(D**2+E*(E+w))/P1*P2))*1/(P1+P2+1j/tau)-((1+(D**2+E*(E+w))/P1*P2))*1/(P1-P2+1j/tau)))

    return I2
    
def integral3(E,w):
    P1 = np.sqrt((E+w)**2-D**2)
    P2 = np.sqrt((E**2-D**2))
    P3 = np.sqrt((E-w)**2-D**2)
    P4 = 1j*np.sqrt(D**2-(E-w)**2)

    I3 = np.tanh(E/(2*k*T)*(((1-(D**2+E*(E-w))/P3*P2))*1/(P3+P2+1j/tau)-((1+(D**2+E*(E-w))/P3*P2))*1/(P3-P2+1j/tau)))
       
    return I3


Tc = 10
T = 5
eps0 = 1
w = 5e9*2*np.pi
k = 1.38e-23
h = 6.63e-34
hbar = h/2*np.pi
D = 1.76*k*Tc
v0 = np.pi*D/(hbar*eps0)
tau = 1/v0

conductivity = 7.3e5

E = np.linspace(0,1,int(1e4))

out1 = [integral1(x,w) for x in E]
out2 = [integral2(x,w) for x in E]
out3 = [integral3(x,w) for x in E]

plt.figure()
plt.scatter(E,abs(out1[:]))
plt.scatter(E,abs(out2[:]))
plt.scatter(E,abs(out3[:]))

"""
if hbar*w <= 2*D:
    J = scint.quad(integral1,D,w+D,args = (w))
else:
    J = scint.quad(integral3,D,w-D,args = (w)) + scint.quad(integral1,w-D,w+D,args = (w))
    
sigZ = 1j/(2*w*tau)*(J+scint.quad(integral2,D,np.inf,args = (w)))
"""




