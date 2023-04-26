# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 13:14:18 2023

@author: 2175469R
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import pandas as pd

def foo(x,m,c,a,b,phi):
    y = m*x+a*np.sin(b*x+phi)**2+c
    return y

path = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\PhaseNoise\LP1550\20mA_15m_3103_Run1.csv"

data = pd.read_csv(path,header = 0)

frequency = data.values[:,1]
mag = data.values[:,2]
power = 10**(mag/10)/1000

#initials = [-7.82002e-08,-69.6999,5,2*np.pi/0.75e8,90]
#initialguess = foo(frequency,initials[0],initials[1],initials[2],initials[3],initials[4])

#plt.figure()
#plt.scatter(frequency,mag)
#plt.plot(frequency,initialguess,color='orange')

#params,covar = opt.curve_fit(foo,frequency,mag,p0 = initials)
#fit = foo(frequency,params[0],params[1],params[2],params[3],params[4])

plt.figure()
plt.scatter(frequency,mag)
#plt.plot(frequency,fit,color='orange')