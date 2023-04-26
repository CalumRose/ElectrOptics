# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 10:49:01 2022

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
                m = (signal[x]-signal[x-1])/(frequency[x]-frequency[x-1])
                half = frequency[x]+(0.5*peak-signal[x])
                fwhm = 2*(half-peakF)
                return [peak,fwhm]
    



def AnritsuRead(path):
    power = pd.read_csv(path,header = 10).values[:,0]
    
    mycsv = list(csv.reader(open(path)))
    
    start = int(mycsv[1][1])
    stop = int(mycsv[1][2])
    points = int(mycsv[7][1])
    
    freq = np.linspace(start,stop,points)
    
    
    return freq,power


folder = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\Anritsu\EOM_Char_25C_16mA"
files = os.listdir(folder)


peaks = []
fwhms = []
freqs = []
powers = []

for file in files:
    freq,power = AnritsuRead(os.path.join(folder,file))
    
    vals = fwhm(power,freq)
    peaks.append(vals[0])
    fwhms.append(vals[1])
    
    freqs.append(file.split('_')[1])
    powers.append(int(file.split('_')[2].split('.')[0].split('d')[0]))
  
fwhm15k = []
fwhm100k = []
fwhm1m = []
fwhm10m = []
fwhm100m = []
fwhm1g = []
fwhm5g = []

p15k = []
p100k = []
p1m = []
p10m = []
p100m = []
p1g = []
p5g = []
    

for i in range(len(files)):
    if freqs[i] == '15kHz':
        fwhm15k.append(fwhms[i]/150)
        p15k.append(powers[i])
    elif freqs[i] == '100kHz':
        fwhm100k.append(fwhms[i]/1000)
        p100k.append(powers[i])
    elif freqs[i] == '1MHz':
        fwhm1m.append(fwhms[i]/1e4)
        p1m.append(powers[i])
    elif freqs[i] == '10MHz':
        fwhm10m.append(fwhms[i]/1e5)
        p10m.append(powers[i])
    elif freqs[i] == '100MHz':
        fwhm100m.append(fwhms[i]/1e6)
        p100m.append(powers[i])
    elif freqs[i] == '1GHz':
        fwhm1g.append(fwhms[i]/1e7)
        p1g.append(powers[i])
    elif freqs[i] == '5GHz':
        fwhm5g.append(fwhms[i]/5e7)
        p5g.append(powers[i])

plt.figure()
plt.plot(p15k,fwhm15k,label = '15kHz',marker = 'x')
plt.plot(p100k,fwhm100k,label = '100kHz',marker = 'x')
plt.plot(p1m,fwhm1m,label = '1MHz',marker = 'x')
plt.plot(p10m,fwhm10m,label = '10MHz',marker = 'x')
plt.plot(p100m,fwhm100m,label = '100MHz',marker = 'x')
plt.plot(p1g,fwhm1g,label = '1GHz',marker = 'x')
plt.plot(p5g,fwhm5g,label = '5GHz',marker = 'x')
plt.legend()
plt.grid()
plt.title('Comparison of FWHM as % of applied rf frequency')
plt.xlabel('Power(dBm)')
plt.ylabel('FWHM(%)')


folder = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\Anritsu\Anritsu_Char"
files = os.listdir(folder)


peaks = []
fwhms = []
freqs = []
powers = []

for file in files:
    freq,power = AnritsuRead(os.path.join(folder,file))
    
    vals = fwhm(power,freq)
    peaks.append(vals[0])
    fwhms.append(vals[1])
    
    freqs.append(file.split('_')[1])
    powers.append(int(file.split('_')[2].split('.')[0].split('d')[0]))
    
fwhm1gMW = []
fwhm5gMW = []

p1gMW = []
p5gMW = []

for i in range(len(files)):
    if freqs[i] == '1GHz':
        fwhm1gMW.append(fwhms[i]/1e7)
        p1gMW.append(powers[i])
    elif freqs[i] == '5GHz':
        fwhm5gMW.append(fwhms[i]/5e7)
        p5gMW.append(powers[i])
        
plt.figure()
plt.scatter(p1g,fwhm1g,label = 'Modulated',marker = 'x')
plt.scatter(p1gMW,fwhm1gMW,label = 'Reference',marker = 'x')
plt.title("Comparison of FWHM for modulated and reference signals at 1GHz")
plt.legend()
plt.xlabel('Power(dBm)')
plt.ylabel('FWHM(%)')

plt.figure()
plt.scatter(p5g,fwhm5g,label = 'Modulated',marker = 'x')
plt.scatter(p5gMW,fwhm5gMW,label = 'Reference',marker = 'x')
plt.title("Comparison of FWHM for modulated and reference signals at 5GHz")
plt.legend()
plt.xlabel('Power(dBm)')
plt.ylabel('FWHM(%)')