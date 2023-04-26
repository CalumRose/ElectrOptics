# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 13:38:34 2022

@author: 2175469R
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft, rfftfreq

def Gaussian(fRange,peak,fwhm):
    
    dist = []
    
    for i in fRange:
        dist.append(1-np.exp(-((i-peak)**2/(2*(fwhm)**2))))
    return dist

fRange = np.linspace(0.1,0.5,24)
resonance = Gaussian(fRange,0.3,0.1)

fRangeAccurate = np.linspace(0.1,0.5,1000)
resonanceAccurate = Gaussian(fRangeAccurate,0.3,0.1)

f = 10
A = 1

peakMA = np.pi/2
delta = 0.0

duration = 20000
samplerate = 100
N = duration*samplerate

x = np.linspace(0,duration,N)
carrier = A*np.sin(f*x)

tp = []

plt.figure()

for i in range(len(fRange)):
    mA = peakMA*resonance[i]
    mod = A*np.sin(f*x + mA*np.sin(fRange[i]*x))

    LO = A*np.sin((f+delta)*x)

    out = (LO + mod)**2

    yf = np.abs(rfft(out))
    xf = rfftfreq(N,1/samplerate)

    xf = [2*np.pi*i for i in xf]
    
    
    
    for j in range(len(yf)-2):
        if (yf[j] <yf[j+1]) & (yf[j+1]>yf[j+2]):
            tp.append(yf[j+1])
            break
     
    plt.scatter(xf,yf)
    plt.xlim([0.01,25])
    plt.title("Fourier transform of modulated output signal",size = 14)
    plt.xlabel("Pump Frequency",size = 14)
    plt.ylabel("Power Spectral Density",size = 14)

tp = [x/max(tp) for x in tp]

plt.figure()
plt.scatter(fRange,tp,label = "Output")
plt.plot(fRangeAccurate,resonanceAccurate,'orange',label = "Resonance")
plt.legend()
plt.title("Simulation of electro-optic readout of resonance",size = 14)
plt.xlabel("Frequency",size = 14)
plt.ylabel("Normalised S21",size = 14)
    #plt.figure()
    #plt.plot(x,out)
    #plt.scatter(x,mod)
    #plt.xlim([0,250])

    
