# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:34:30 2022

@author: 2175469R
"""

import os
import numpy as np
import scipy.optimize as opt
import pandas as pd
import matplotlib.pyplot as plt

def Gaussian(freqRange,p,f,fwhm):
    
    stdev = fwhm/(2*np.sqrt(2*np.log(2)))
    
    power = []
    
    for i in freqRange:
        power.append(p*np.exp(-((i-f)**2/(2*(stdev)**2))))
    return np.array(power)

def advGaussFit(freq,traceLin,initials):
    params, cov = opt.curve_fit(Gaussian,freq,traceLin,p0 = initials)
    out = Gaussian(freq,params[0],params[1],params[2])
   
    return params[0],params[1],params[2]

path = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\Cold_PD\2911.csv"

files = os.listdir(path)

initials = [0.4,1550.55,0.1]

power = []
peak = []
fwhm = []

for file in files:
        df = pd.read_csv(os.path.join(path,file),delimiter = ';',header = 92)
        
        k = df.index
        k=list(k[0:-1])
        k = [1e7/float(i) for i in k]

        
        I = df.values[:,0]
        I = (I[0:-1])
        
        

        
        params = advGaussFit(k,I,initials)
        initials = params
        
        out = Gaussian(k,params[0],params[1],params[2])

        
        power.append(initials[0])
        peak.append(initials[1])
        fwhm.append(initials[2])

plt.figure()    
plt.scatter(np.array(range(len(power)))*10,power)
plt.title('Power throughout cooldown')
plt.xlabel('Time(minutes)')
plt.ylabel('Power(mW)')
plt.grid()

plt.figure()    
plt.scatter(np.array(range(len(peak)))*10,peak)
plt.title('Peak wavelength  throughout cooldown')
plt.xlabel('Time(minutes)')
plt.ylabel('Wavelength(nm)')
plt.grid()

plt.figure()    
plt.scatter(np.array(range(len(fwhm)))*10,fwhm)
plt.title('FWHM  throughout cooldown')
plt.xlabel('Time(minutes)')
plt.ylabel('FWHM(nm)')
plt.grid()


        
        
        
        
