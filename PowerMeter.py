# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 10:14:39 2023

@author: admin
"""

import pyvisa as visa
import numpy as np

rm = visa.ResourceManager()
rm.list_resources()
PM = rm.open_resource('USBInstrument3')

power = []
for i in range(20):
    power.append(float(PM.query('MEAS:POW?')))
    

P = np.mean(np.array(power))
