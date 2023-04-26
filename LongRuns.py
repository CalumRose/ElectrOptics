# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 11:20:24 2022

@author: 2175469R
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat


def readCSV(path):
    df = pd.read_csv(path)
    times = df.values[:,1]
    powers = np.array(df.values[:,2])
    fwhms = df.values[:,3]
    peaks = df.values[:,4]
    
    #powers = [10*math.log(x,10)+30 for x in powers]
    
    powVar = stat.variance(powers)
    fwhmVar = stat.variance(fwhms)
    peakVar = stat.variance(peaks)
    
    plt.figure()
    plt.scatter(times,peaks)
    plt.title('Peak frequency of modulated signal with bias-tee, variance = %f Hz' %peakVar)
    plt.xlabel('Time(s)')
    plt.ylabel('Frequency(Hz)')
    plt.grid()
    
    plt.figure()
    plt.scatter(times,fwhms)
    plt.title('FWHM of modulated signal with bias-tee, variance = %f Hz' %peakVar)
    plt.xlabel('Time(s)')
    plt.ylabel('FWHM(Hz)')
    plt.grid()
    
    plt.figure()
    plt.scatter(times,powers)
    plt.title('Power of modulated signal with bias-tee, variance = %f dBm' %powVar)
    plt.xlabel('Time(s)')
    plt.ylabel('Power(dBm)')
    plt.grid()
    
    return times,powers,fwhms,peaks


path = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\Anritsu\LongRuns\DIRECT_5G_-20db_n500_BW20M.csv"

readCSV(path)