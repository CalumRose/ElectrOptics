# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:47:18 2023

@author: admin
"""

import numpy as np
import qkit
import matplotlib.pyplot as plt
import pandas as pd

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
    

def writeCSV(d,path):
    df = pd.DataFrame(data = d)
    
    df.to_csv(path)

qkit.cfg['load_visa'] = True
qkit.start()

Rigol = qkit.instruments.create('Rigol','Rigol_DSG3060',address='USB0::0x1AB1::0x0992::DSG3A183600072::0::INSTR')
Rigol.reset()

ESA = qkit.instruments.create('ESA','Anritsu_MS2830A',address='USB0::0x0B5B::0x0006::6201585505::0::INSTR')
ESA.reset()

