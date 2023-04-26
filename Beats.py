# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:18:34 2022

@author: 2175469R
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft,rfftfreq


def Gaussian(fRange,peak,fwhm):
    
    dist = []
    
    for i in fRange:
        dist.append(1-np.exp(-((i-peak)**2/(2*(fwhm)**2))))
    return dist


fC = 190e12


duration = (5/8e9)
samplerate = 1e6/duration

proberange = np.linspace(4e9,8e9,5)
resonator = Gaussian(proberange,6e9,5e8)

plt.figure()
plt.scatter(proberange,resonator)

x = np.linspace(0,1,int(duration*samplerate))
x = x*duration


carrier = np.sin(fC*x)

mod = []
out = []
LO = []
outf  = []

xf = rfftfreq(int(samplerate*duration),1/samplerate)

plt.figure()

for i in range(len(proberange)):
    M = resonator[i]*np.sin(proberange[i]*x)
    O = np.sin(x + M)
    L = np.sin((fC-proberange[i])*x)
    
    mod.append(M)
    out.append(O)
    LO.append(L)


    hdyne = []

    for j in range(len(x)):
        hdyne.append(out[i]+LO[i])
        
    
    

    OF = rfft(out[i])
    outf.append(OF)   

    plt.scatter(xf, np.abs(outf[i]))


