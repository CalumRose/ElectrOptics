# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:22:02 2023

@author: admin
"""

import numpy as np
import qkit
import matplotlib.pyplot as plt
import pandas as pd
import pyvisa as visa
import time

qkit.cfg['load_visa'] = True
qkit.start()

ESA = qkit.instruments.create('ESA','Anritsu_MS2830A',address='USB0::0x0B5B::0x0006::6201585505::0::INSTR')
ESA.reset

rm = visa.ResourceManager()
rm.list_resources()
PM = rm.open_resource('USBInstrument3')

bias = np.linspace(1,4,31)
laserPower = []
mainPeaks = []
harmonicPeaks = []

for i in range(len(bias)):
    mainTemp = []
    harmonicTemp = []
    laserTemp = []
    for j in range(20):
        laserTemp.append(float(PM.query('MEAS:POW?')))
        
        ESA.do_set_centerfreq(5e9)
        ESA.do_set_freqspan(20e6)
        vals = ESA.get_trace(1)
        mainTemp.append(max(vals))
        
        ESA.do_set_centerfreq(10e9)
        ESA.do_set_freqspan(20e6)
        vals = ESA.get_trace(1)
        harmonicTemp.append(max(vals))
        
        time.sleep(0.2)
        
    mainPeaks.append(np.mean(mainTemp))
    harmonicPeaks.append(np.mean(harmonicTemp))
    laserPower.append(np.mean(laserTemp))
    time.sleep(1)
    print('Set bias to ' + str(bias[i+1]))
    input('enter to coninue')
    
    

plt.figure()
plt.scatter(bias,mainPeaks)
folder = r'C:\Users\admin\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\BiasPoint'
filename = '\InensityModulatorHarmonics.csv'
df = pd.DataFrame({'Laser': laserPower, 'Signal': harmonicPeaks, 'Harmonic': mainPeaks})
df.to_csv(folder+filename)