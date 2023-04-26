# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:38:15 2022

@author: 2175469R
"""

import csv
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat


folder = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\EOM_Noise\LongNoRF_15mA"

files = os.listdir(folder)
temp = []
current = []
wl = []
I = []
fwhm = []
fwhmVar = []
P = []
Pvar = []
lamda = []
lamdaVar = []
time = []



for file in files:
    if file[-5] == '0':
        df = pd.read_csv(os.path.join(folder,file),delimiter = ';',header = 92)
        
        k = df.index
        k=list(k[0:-1])
        k = [1e7/float(i) for i in k]
        wl.append(k)
        
        Int = df.values[:,0]
        Int = (Int[0:-1])
        I.append(Int)
    
    if len(file) > 20:
        if file[31] == 'e':
            df = pd.read_csv(os.path.join(folder,file),delimiter = ';',header = 1)
            fwhm.append(df.values[:,3])
            fwhmVar.append(stat.variance(df.values[:,3]))
            time.append(df.values[:,1])
            
        if file[31] == 'o':
            df = pd.read_csv(os.path.join(folder,file),delimiter = ';',header = 1)
            P.append(df.values[:,2])
            Pvar.append(stat.variance(df.values[:,2])*100/(np.mean(df.values[:,2])))
            
        if file[31] == 'a':
            df = pd.read_csv(os.path.join(folder,file),delimiter = ';',header = 1)
            lamda.append(df.values[:,2])
            lamdaVar.append(stat.variance(df.values[:,2]))
            
        
plt.figure()
plt.scatter(range(len(P[0])),P[0])
plt.title('Power variation over 10minutes measured with OSA')
plt.ylabel('Power (mA)')
plt.xlabel('time(s)')

plt.figure()
plt.scatter(range(len(fwhm[0])),fwhm[0])
plt.title('FWHM variation over 10minutes measured with OSA')
plt.ylabel('fwhm (nm)')
plt.xlabel('time(s)')

plt.figure()
plt.scatter(range(len(lamda[0])),lamda[0])
plt.title('Peak wavelength variation over 10minutes measured with OSA')
plt.ylabel('Wavelength (nm)')
plt.xlabel('time(s)')
 