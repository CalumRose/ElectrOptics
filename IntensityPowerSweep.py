# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 13:29:48 2023

@author: 2175469R
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
Keith = qkit.instruments.create('Keith','Keithley_2200',address='USB0::0x05E6::0x2200::9210782::0::INSTR')
Keith.reset()
ESA = qkit.instruments.create('ESA','Anritsu_MS2830A',address='USB0::0x0B5B::0x0006::6201585505::0::INSTR')
ESA.reset()
PowerMeter = qkit.instruments.create('PowerMeter','ThorLabs_PM100D',address='USB0::0x1313::0x8078::P0039860::0::INSTR')
PowerMeter.reset()

freq = 5e9
rfRange = np.linspace(-50,20,71)
keithRange = np.linspace(0.5,2,16)
ESACenterFreq = freq
ESAFreqSpan = 4e8

TransmittedFWHM = np.zeros([len(keithRange),len(rfRange)])
TransmittedPower = np.zeros([len(keithRange),len(rfRange)])

Rigol.do_set_frequency(5e9)
Rigol.do_set_power(-100)
Rigol.do_set_state(1)

Keith.set_output(1)

ESA.do_set_centerfreq(ESACenterFreq)
ESA.do_set_freqspan(ESAFreqSpan)

PowerMeter.do_set_wavelength(1550)

folder = r'C:\Users\2175469R\OneDrive - University of Glasgow\Documents - Quantum Circuit Group\shared folders\ElectroOptic\data\IntensityPowerSweeps'

for i in range(len(keithRange)):
    Keith.do_set_voltage(keithRange[i])
    for j in range(len(rfRange)):
        Rigol.do_set_power(rfRange[j])
        opticalPower = PowerMeter.do_measure_power()
        freqs = ESA.get_frequencies()
        vals = ESA.get_trace(1)
        
        filename = str(freq/1e9) + 'GHz_' + str(rfRange[j]) + 'dBm_' + str(opticalPower/1e6) + 'uW.csv'
        df = pd.DataFrame({'Frequency': freqs, 'Power': vals})
        df.to_csv(folder+filename)
        
        params = fwhm(vals,freqs)
        
        TransmittedPower[i,j] = params[0]
        TransmittedFWHM[i,j] = params[1]
        
        
        