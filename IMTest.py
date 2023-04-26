# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 13:25:41 2022

@author: 2175469R
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft, rfftfreq

f = 5
A = 1

mf = 0.3
mArange = np.linspace(0.4,2,5)

delta = 0.1

duration = 10000
samplerate = 10
N = duration*samplerate

x = np.linspace(0,duration,N)

carrier = A*np.sin(f*x)
plt.figure()
for mA in mArange:
    mw = mA*np.sin(mf*x)
    
    mod = ((1-abs(mw))*carrier)**2
    
    LO = A*np.sin((f)*x+np.pi/2)
    
    out = (LO + mod)**2
    
    yf = rfft(mod)
    xf = rfftfreq(N,1/samplerate)
    
    xf = [2*np.pi*i for i in xf]

    plt.scatter(xf,np.abs(yf),label = str(mA))
    plt.xlim([0.01,4])
    plt.title("Fourier transform of modulated output signal",size = 14)
    plt.xlabel("Frequency",size = 14)
    plt.ylabel("Power Spectral Density",size = 14)
    plt.legend()

#print(abs(yf[955]))



