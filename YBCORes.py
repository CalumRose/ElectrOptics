# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 15:58:59 2022

@author: 2175469R
"""

import numpy as np

eta = 0.9
tau = 1e-12
q = 3.2e-19
me = 1.8e-30


h = 100e-9
w = 5e-6
l = 3e-3

J = 2e10
Tc = 70
Ic = J*(h*w)

k = 1.38e-23
D = 4.8e-21

T = 55
I = 10e-3
f = 5e9
omega = f*2*np.pi

Rsq = 100

LkSq = 2e-12

Lk = LkSq*l/w
R = Rsq*l/w

n = me*l/(Lk*q**2*h*w)

Res = eta*tau*I/(2*D*w*h*l*n)*1j*omega*Lk*R/(1j*omega*Lk+R)


print(abs(Res))
Pin = 0.001
Pout = (abs(Res)*Pin)**2/R