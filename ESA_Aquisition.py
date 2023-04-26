# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:23:07 2023

@author: 2175469R
"""

import qkit
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def writeCSV(d,path):
    df = pd.DataFrame(data = d)
    
    df.to_csv(path)

qkit.cfg['load_visa'] = True
qkit.start()
ESA = qkit.instruments.create('ESA','Anritsu_MS2830A',address='USB0::0x0B5B::0x0006::6201585505::0::INSTR')

ESA.do_set_centerfreq(2e8)
ESA.do_set_freqspan(4e8)

freqs = ESA.get_frequencies()

vals = np.zeros([len(freqs)])


single = 1
if single == 0:
    for i in range(100):
        vals = vals + ESA.get_trace(1)
else:
    vals = ESA.get_trace(1)

#vals = vals/100

#vals = 10**(vals/10)/1000

date = '3103'
laserCurrent = '20mA'
#mwPower = 'noMW'
#freq = 'noMW'
PD = 'PM'
Run = 'Run2'
folder = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\PhaseNoise\LP1550/"
#filename = 'NoLaser'
#filename  = "LP1550"+'_'+laserCurrent+'_'+PD
filename = laserCurrent+'_'+PD+'_'+date+'_'+Run+'.csv'
path = folder + filename

data = pd.DataFrame({'Frequency': freqs, 'Power': vals})

writeCSV(data,path)

channelWidth = freqs[1]-freqs[0]
rtHz = np.sqrt(channelWidth)
noise = vals/rtHz

plt.figure()
plt.scatter(freqs,vals)
plt.grid()

plt.figure()
plt.scatter(freqs,noise)
plt.grid()
