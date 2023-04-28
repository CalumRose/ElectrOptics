# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 13:29:48 2023

@author: 2175469R
"""

import numpy as np
import qkit
import matplotlib.pyplot as plt

qkit.config['load_visa'] = True
qkit.start()
Rigol = qkit.instruments.create('Rigol','RIGOL_DSG3060',address='Instrument4')
Keith = qkit.instruments.create('Keith','Keithley_2200',address='Instrument2')
ESA = qkit.instruments.create('ESA','Anritsu_MS2830A',address='Instrument1')
PowerMeter = qkit.instruments.create('PowerMeter','Thorlabs_PM100D',address='Instrument3')

freq = 5e9
rfRange = np.linspace(-50,20,71)
keithRange = np.linspace(0.5,2,16)
ESACenterFreq = freq
ESAFreqSpan = 4e8

Rigol.do_set_frequency(freq)
ESA.do_set_centerfreq(ESACenterFreq)
ESA.do_set_freqspan(ESAFreqSpan)

TransmittedFWHM = np.zeros([len(rfRange),len(keithRange)])
TransmittedPower = np.zeros([len(rfRange),len(keithRange)])

