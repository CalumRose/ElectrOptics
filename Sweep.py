# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:10:47 2023

@author: 2175469R
"""

import pyvisa as visa
import numpy as np
import qkit
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
import matplotlib.pyplot as plt

def writeCSV(d,path):
    df = pd.DataFrame(data = d)
    
    df.to_csv(path)
    
qkit.cfg['load_visa'] = True
qkit.start()
ESA = qkit.instruments.create('ESA','Anritsu_MS2830A',address='USB0::0x0B5B::0x0006::6201585505::0::INSTR')
ESA.do_set_centerfreq(3.8e9)
ESA.do_set_freqspan(2e8)

rm = visa.ResourceManager()
inst = rm.open_resource('USBInstrument2')


freqrange = np.linspace(3.75e9,3.875e9,201)
inst.write(':SOUR:LEV 20')
inst.write(':OUTP:STAT 1')


peaks = []

for val in freqrange:
    inst.write('SOUR:FREQ '+str(val))
    time.sleep(1)
    temp = []
    for i in range(40):
        temp.append(max(ESA.get_trace(1)))
    peaks.append(np.mean(temp))


path = r"C:\Users\admin\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\PhaseModulation\CavityMeasurements\August\IntMod.csv"
data = pd.DataFrame({'Frequency': freqrange, 'Power': peaks})

writeCSV(data,path)
    
plt.figure()
plt.scatter(freqrange,peaks)

