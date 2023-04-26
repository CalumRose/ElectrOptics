# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 18:15:17 2022

@author: 2175469R
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft, rfftfreq



ldPower = 2e-3

mwFreq = 1e9
mwVoltage = 4
vPi = 5.6


duration = 1e-7
samplerate = 10000/1e-7
N = int(duration*samplerate)

t = np.linspace(0,1e-7,10000)

mwSignal = mwVoltage*np.sin(mwFreq*t)

modulation = ldPower*(1+np.sin(np.pi*mwSignal/vPi))

yf = np.abs(rfft(modulation))
xf = rfftfreq(N,1/samplerate)

xf = [2*np.pi*i for i in xf]

plt.figure()
plt.plot(t,modulation)
plt.title("Time domain output from intensity modulator driven by 1GHz")
plt.xlabel("Time(s)")

plt.figure()
plt.scatter(xf,yf)
plt.title("Frequency domain output from intensity modulator driven by 1GHz")
plt.xlabel("Frequency(Hz)")
