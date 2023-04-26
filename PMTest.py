# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 14:41:50 2022

@author: 2175469R
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft, rfftfreq

f = 1
A = 1

mf = 0.3
mA = 1

delta = 0.05

duration = 10000
samplerate = 10
N = duration*samplerate

x = np.linspace(0,duration,N)

carrier = A*np.sin(f*x)

mod = A*np.sin(f*x + mA*np.sin(mf*x))

LO = A*np.sin((f+mf/2+delta)*x)

out = (LO + mod)**2

yf = rfft(out)
xf = rfftfreq(N,1/samplerate)

xf = [2*np.pi*i for i in xf]


plt.figure()
plt.plot(x,out)
#plt.scatter(x,mod)
plt.xlim([0,250])
plt.title("Time domain simulation of phase modulator characterisation, with local oscillator, delta=0.05")
plt.xlabel("Time/s")
plt.ylabel("Amplitude")

plt.figure()
plt.scatter(xf,np.abs(yf))
plt.xlim([0.01,3])
plt.title("Time domain simulation of phase modulator characterisation, with local oscillator, delta=0.05")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")