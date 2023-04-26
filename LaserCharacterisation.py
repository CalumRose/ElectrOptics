# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 10:16:04 2022

@author: 2175469R
"""

import csv
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat


folder = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\LaserCharacterisation"

combs = os.listdir(folder)

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

for combo in combs:
    temp.append(combo.split("K_")[0])
    current.append(combo.split("_")[1].split("m")[0])
    
    files = os.listdir(os.path.join(folder,combo))
    print(combo)

    
    for file in files:
        if file[-5] == '0':
            df = pd.read_csv(os.path.join(folder,combo,file),delimiter = ';',header = 92)
            
            k = df.index
            k=list(k[0:-1])
            k = [1e7/float(i) for i in k]
            wl.append(k)
            
            Int = df.values[:,0]
            Int = (Int[0:-1])
            I.append(Int)
        
        if len(file) > 20:
            if file[31] == 'e':
                df = pd.read_csv(os.path.join(folder,combo,file),delimiter = ';',header = 1)
                fwhm.append(np.mean(df.values[:,3]))
                fwhmVar.append(stat.variance(df.values[:,3]))
                
            if file[31] == 'o':
                df = pd.read_csv(os.path.join(folder,combo,file),delimiter = ';',header = 1)
                P.append(np.mean(df.values[:,2]))
                Pvar.append(stat.variance(df.values[:,2])*100/(np.mean(df.values[:,2])))
                
            if file[31] == 'a':
                df = pd.read_csv(os.path.join(folder,combo,file),delimiter = ';',header = 1)
                lamda.append(np.mean(df.values[:,2]))
                lamdaVar.append(stat.variance(df.values[:,2]))
                
centreF10mA = []
centreF15mA = []
centreF20mA = []

P10mA = []
P15mA = []
P20mA = []

fwhm10mA = []
fwhm15mA = []
fwhm20mA = []

temps = [20,22,24,26,28]

                
plt.figure()
"""make variables with data we want and creat table?"""
for i in range(len(current)):
    if current[i] == '10':
        centreF10mA.append(lamdaVar[i]*1e6)
        P10mA.append(Pvar[i])
        fwhm10mA.append(fwhmVar[i]*1e6)
    
    if current[i] == '15':
        plt.plot(wl[i][:],I[i][:],label = temp[i] + "C")
        plt.legend(fontsize = 20)
        plt.xlabel("Wavelength(nm)",size = 25)
        plt.ylabel("Intensity(mW)",size = 25)
        plt.title("Spectra at varying of temperature with 15mA bias",size = 25)
        plt.grid()
        plt.tick_params(axis = 'both', direction = 'in',labelsize = 25,length = 10,width = 2,bottom=True, top=True, left=True, right=True)

        centreF15mA.append(lamdaVar[i]*1e6)
        P15mA.append(Pvar[i])
        fwhm15mA.append(fwhmVar[i]*1e6)
        
    if current[i] == '20':
        centreF20mA.append(lamdaVar[i]*1e6)
        P20mA.append(Pvar[i])
        fwhm20mA.append(fwhmVar[i]*1e6)

fwhm10mA[0] = 0.0007
centreF10mA[0] = 0.013

plt.figure()
plt.scatter(temps,centreF10mA,label = '10mA',marker = '.',s = 150)
plt.plot(temps,centreF10mA)
plt.scatter(temps,centreF15mA,label = '15mA',marker = 'v',s = 70)
plt.plot(temps,centreF15mA)
plt.scatter(temps,centreF20mA,label = '20mA',marker = ',',s = 70)
plt.plot(temps,centreF20mA)
plt.title('Peak Wavelength Variance',size = 25)
plt.xlabel('Temperature(C)',size = 25)
plt.ylabel('Variance(fm)',size = 25)
plt.legend(fontsize = 20)
plt.grid()
plt.tick_params(axis = 'both', direction = 'in',labelsize = 25,length = 10,width = 2,bottom=True, top=True, left=True, right=True)

plt.figure()
plt.scatter(temps,P10mA,label = '10mA',marker = '.',s = 150)
plt.plot(temps,P10mA)
plt.scatter(temps,P15mA,label = '15mA',marker = 'v',s = 70)
plt.plot(temps,P15mA)
plt.scatter(temps,P20mA,label = '20mA',marker = ',',s = 70)
plt.plot(temps,P20mA)
plt.title('Laser Power variance',size = 25)
plt.xlabel('Temperature(C)',size = 25)
plt.ylabel('Variance(%)',size = 25)
plt.legend(fontsize = 20)
plt.grid()
plt.tick_params(axis = 'both', direction = 'in',labelsize = 25,length = 10,width = 2,bottom=True, top=True, left=True, right=True)

plt.figure()
plt.scatter(temps,fwhm10mA,label = '10mA',marker = '.',s = 150)
plt.plot(temps,fwhm10mA)
plt.scatter(temps,fwhm15mA,label = '15mA',marker = 'v',s = 70)
plt.plot(temps,fwhm15mA)
plt.scatter(temps,fwhm20mA,label = '20mA',marker = ',',s = 70) 
plt.plot(temps,fwhm20mA)       
plt.title('Full-width half-maximum variance',size = 25)
plt.xlabel('Temperature(C)',size = 25)
plt.ylabel('Variance(fm)',size = 25)     
plt.legend(fontsize = 20)
plt.grid()
plt.tick_params(axis = 'both', direction = 'in',labelsize = 25,length = 10,width = 2,bottom=True, top=True, left=True, right=True)

"""
plt.grid()
plt.scatter(I,VData,color = 'k',label = "Data")
plt.plot(I,VFit,'r',linewidth = 2,label = "Fit")
plt.xlabel("Current (I/I$_c$)",size = 25)
plt.ylabel("Voltage (V/V$_c$)",size = 25)
plt.legend(fontsize = 20)
plt.tick_params(axis = 'both', direction = 'in',labelsize = 25,length = 10,width = 2,bottom=True, top=True, left=True, right=True)
"""

plt.figure()
for i in range(len(temp)):
    if temp[i] == '24':
        plt.plot(wl[i][:],I[i][:],label = current[i]+'mA')
        plt.legend(fontsize = 20)
        plt.xlabel("Wavelength(nm)",size = 25)
        plt.ylabel("Intensity(mW)",size = 25)
        plt.title("Spectra at varying of bias current ",size = 25)
        plt.tick_params(axis = 'both', direction = 'in',labelsize = 25,length = 10,width = 2,bottom=True, top=True, left=True, right=True)
        plt.grid()

plt.figure()
current = [5, 10, 15, 20]
fwhm = [59,58,59,57]
plt.scatter(current,fwhm)
plt.xlabel("Bias Current(mA)",size = 25)
plt.ylabel("FWHM(pm)",size = 25)
plt.title("FWHM at varying bias current ",size = 25)
plt.tick_params(axis = 'both', direction = 'in',labelsize = 25,length = 10,width = 2,bottom=True, top=True, left=True, right=True)
plt.grid()