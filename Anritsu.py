# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 15:27:27 2022

@author: 2175469R
"""

import csv
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat



def fwhm(signal, frequency):
    peak = max(signal)
    peakInd = signal.argmax()
    peakF = frequency[peakInd]
    
    signal = 10**(signal/10)/1000
    
    #plt.scatter(frequency,signal)
    
    for x in range(len(signal)):
        if x > peakInd:
            if signal[x] < 0.5*signal[peakInd]:
                grad = (signal[x+1]-signal[x])/(frequency[x+1]-frequency[x])
                c = frequency[x]*grad + signal[x]
                fwhm = grad*0.5*signal[peakInd] + c
                return peak,fwhm
    





#freqRangeL = np.linspace(-141016,2.5e8,10001)
#freqRangeS = np.linspace(1e6,1e9,10001)

#laserFile = r"D:\Anritsu Corporation\Signal Analyzer\User Data\Trace Data\Spectrum Analyzer\100MHz-10dbm.csv"
#sigGenFile = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\Anritsu\NoLaser_100MHz_-10dBm.csv"
"""
laser = pd.read_csv(laserFile,header = 10).values[:,0]
sigGen = pd.read_csv(sigGenFile,header = 10).values[:,0]

plt.figure()
peakL,fwhmL = fwhm(laser,freqRangeL)
peakS,fwhmS = fwhm(sigGen,freqRangeS)



freqRangeL = (freqRangeL/1e6)
freqRangeS = (freqRangeS/1e6)


plt.figure()
plt.scatter(freqRangeS,sigGen, label = 'Modulating signal:-10dBm,1MHz FWHM')
plt.scatter(freqRangeL,laser,label = 'Photodetector output:-39dbm,1MHz FWHM')
plt.title('Photodetector response to laser modulated at 100MHz',size = 25)
plt.xlabel('Frequecy(MHz)',size = 25)
plt.ylabel('Power(dBm)',size = 25)
plt.legend(fontsize = 20)
plt.grid()
plt.tick_params(axis = 'both', direction = 'in',labelsize = 25,length = 10,width = 2,bottom=True, top=True, left=True, right=True)

"""




#freqRangeL = np.linspace(-141016,3e9,10001)
#freqRangeS = np.linspace(1e6,1.5e9,10001)

#laserFile = r"D:\Anritsu Corporation\Signal Analyzer\User Data\Trace Data\Spectrum Analyzer\500MHz-10dbm.csv"
#sigGenFile = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\Anritsu\NoLaser_500MHz_-10dBm.csv"
"""

laser = pd.read_csv(laserFile,header = 10).values[:,0]
sigGen = pd.read_csv(sigGenFile,header = 10).values[:,0]

plt.figure()
peakL,fwhmL = fwhm(laser,freqRangeL)
peakS,fwhmS = fwhm(sigGen,freqRangeS)



freqRangeL = (freqRangeL/1e6)
freqRangeS = (freqRangeS/1e6)


plt.figure()
plt.scatter(freqRangeS,sigGen, label = 'Modulating signal:-10dBm,33MHz FWHM')
plt.scatter(freqRangeL,laser,label = 'Photodetector output:-39dbm,36MHz FWHM')
plt.title('Photodetector response to laser modulated at 500MHz',size = 25)
plt.xlabel('Frequecy(MHz)',size = 25)
plt.ylabel('Power(dBm)',size = 25)
plt.legend(fontsize = 20)
plt.grid()
plt.tick_params(axis = 'both', direction = 'in',labelsize = 25,length = 10,width = 2,bottom=True, top=True, left=True, right=True)

"""




freqRange = np.linspace(1e6,2.5e9,10001)
laserFile = r"D:\Anritsu Corporation\Signal Analyzer\User Data\Trace Data\Spectrum Analyzer\1GHz-10dbm.csv"
sigGenFile = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\Anritsu\NoLaser_1GHz_-10dBm.csv"


laser = pd.read_csv(laserFile,header = 10).values[:,0]
sigGen = pd.read_csv(sigGenFile,header = 10).values[:,0]

plt.figure()
peakL,fwhmL = fwhm(laser,freqRange)
peakS,fwhmS = fwhm(sigGen,freqRange)



freqRange = (freqRange/1e9)


plt.figure()
plt.scatter(freqRange,sigGen, label = 'Modulating signal:-10dBm,35MHz FWHM')
plt.scatter(freqRange,laser,label = 'Photodetector output:-37dbm,30MHz FWHM')
plt.title('Photodetector response to laser modulated at 1GHz',size = 25)
plt.xlabel('Frequecy(GHz',size = 25)
plt.ylabel('Power(dBm)',size = 25)
plt.legend(fontsize = 20)
plt.grid()
plt.tick_params(axis = 'both', direction = 'in',labelsize = 25,length = 10,width = 2,bottom=True, top=True, left=True, right=True)

