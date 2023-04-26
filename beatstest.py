# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 13:30:33 2022

@author: 2175469R
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft,rfftfreq



duration = 50
samplerate = 100
N = duration*samplerate


modfreq = 0.1
modamp = 0.5

x = np.linspace(0,duration,N)

carrier = np.sin(x)

mod = modamp*np.sin(modfreq*x)

out = np.sin(x+mod)

