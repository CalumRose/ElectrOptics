# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 16:11:56 2022

@author: 2175469R
"""

import numpy as np

eta = 0.9
tau = 116e-11
q = 3.2e-19
me = 1.8e-30


h = 20e-9
w = 5e-6
l = 3e-3

J = 1.4e11
Tc = 10
Ic = J*(h*w)

k = 1.38e-23
D = 1.76*k*Tc

T = 0.5*Tc
I = 0.5*Ic
f = 5e9
omega = f*2*np.pi


res = 1.37e-6
Rsq = res/h

LkSq = 10e-12
#LkSq = Rsq*h/(2*np.pi**2*np.tanh(D/(2*k*T)))

Lk = LkSq*l/w
R = Rsq*l/w

n = me*l/(Lk*q**2*h*w)

Res = eta*tau*I/(2*D*w*h*l*n)*1j*omega*Lk*R/(1j*omega*Lk+R)


print(abs(Res))
Pin = 0.001
Pout = (abs(Res)*Pin)**2/R

print(Pout/Pin)
