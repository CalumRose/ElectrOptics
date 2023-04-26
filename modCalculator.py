# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 14:21:12 2022

@author: 2175469R
"""

import numpy as np

laserPower = 15e-3


rfPower = 0
rfLin = 10**(rfPower/10)/1000

Vrms = np.sqrt(rfLin*50)

Vtheta = 5

modFrac = Vrms/Vtheta

responsivity = 0.9

IOut = responsivity*modFrac*laserPower
rfOut = IOut**2*50

rfdBm = 10*np.log10(rfOut)+30

print(rfdBm)