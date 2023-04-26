# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:01:34 2022

@author: 2175469R
"""

import csv
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


def AnritsuRead(path):
    freq = pd.read_csv(path,header = 0).values[:,1]
    power = pd.read_csv(path,header = 0).values[:,2]
    """
    mycsv = list(csv.reader(open(path)))
    
    start = int(mycsv[1][1])
    stop = int(mycsv[1][2])
    points = int(mycsv[7][1])
    
    freq = np.linspace(start,stop,points)
    """
    
    return freq,power

path = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\PhaseNoise\ModulatorOnly.csv"
freq,power = AnritsuRead(path)
plt.figure()
plt.plot(freq,power)

# mod = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\PhaseModulation\CavityMeasurements\modulated.csv"
# rf = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\PhaseModulation\CavityMeasurements\direct.csv"

# modf,modp = AnritsuRead(mod)
# rff,rfp = AnritsuRead(rf)

# modp = [x+40 for x in modp]
# rfp = [x+20 for x in rfp]

# modf = [x/1e9 for x in modf]
# rff = [x/1e9 for x in rff]

# plt.figure()
# plt.scatter(modf,modp,color = 'red',marker = 'x',s = 100,label = 'EOM Measurement')
# plt.plot(rff,rfp,color='black',label = 'Direct Measuement')
# plt.title('S21 of 3.82GHz resonance cavity',size=20)
# plt.xlabel('Frequency(GHz)',size=20)
# plt.ylabel('S21(dB)',size=20)
# plt.legend(fontsize=20)
#  plt.grid()
