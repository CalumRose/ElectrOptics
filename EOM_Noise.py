# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 12:58:51 2022

@author: 2175469R
"""

import csv
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat


folder = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\LaserCharacterisation\EOM_Noise"

combs = os.listdir(folder)
labels = []
fwhm = []
power = []
lamda = []

fig1,ax1 = plt.subplots()
fig2,ax2 = plt.subplots()
fig3,ax3 = plt.subplots()

for i in range(len(combs)):
    if combs[i] == 'NoRF':
        labels.append(combs[i])
    else:
        labels.append(combs[i].replace('n','-'))    
    
    files = os.listdir(os.path.join(folder,combs[i]))
    
    for file in files:
        if file[31] == 'e':
            df = pd.read_csv(os.path.join(folder,combs[i],file),delimiter = ';',header = 1)
            fwhm.append(np.mean(df.values[:,3]*1e2/1550))
            #fwhmVar.append(stat.variance(df.values[:,3]))
            ax1.plot(df.values[:,3],label = labels[i])
            ax1.legend()
            
        if file[31] == 'o':
            df = pd.read_csv(os.path.join(folder,combs[i],file),delimiter = ';',header = 1)
            power.append(np.mean(df.values[:,2]))
            #Pvar.append(stat.variance(df.values[:,2])*100/(np.mean(df.values[:,2])))
            ax2.plot(df.values[:,2],label = labels[i])
            ax2.legend()

        if file[31] == 'a':
            df = pd.read_csv(os.path.join(folder,combs[i],file),delimiter = ';',header = 1)
            lamda.append(np.mean(df.values[:,2]))
            #lamdaVar.append(stat.variance(df.values[:,2]))
            ax3.plot(df.values[:,2],label = labels[i])
            ax3.legend()

powers = []            
for l in labels[0:-1]:
    powers.append(int(l.split('d')[0]))

plt.figure()
plt.scatter(powers,fwhm[0:-1])
plt.title('FWHM of laser spectrum with varying RF modulation')
plt.xlabel('RF Power')
plt.ylabel('FWHM (% of wavelength)')

plt.figure()
plt.scatter(powers,power[0:-1])
plt.title('Laser power with varying RF modulation')
plt.xlabel('RF Power')
plt.ylabel('Power (mW)')

plt.figure()
plt.scatter(powers,lamda[0:-1])
plt.title('Peak wavekength with varying RF modulation')
plt.xlabel('RF Power')
plt.ylabel('Laser peak wavelength (nm)')
