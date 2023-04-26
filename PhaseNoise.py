# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 10:34:41 2023

@author: 2175469R
"""

import csv
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat


file = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\LaserCharacterisation\24K_20mA\24-20-000000000.csv"

df = pd.read_csv(file,delimiter = ';',header = 92)

k = df.index
k=list(k[0:-1])
wl = [1e-2/float(i) for i in k]

f = [3e8/x for x in wl]


Int = df.values[:,0]
Int = (Int[0:-1])
plt.figure()
plt.scatter(f,Int)



























"""
t = np.linspace(0,1e-5,100000)
import matplotlib.pyplot as plt
n = 1.46
lamda = 1550
k = np.pi*2/lamda
L = 1

A = 1
omega = 20e6
dv = np.sin(omega*t)
c = 3e8

dPhi = 2*np.pi*n*L*dv/c

#plt.figure()
#plt.scatter(t,dv)
#plt.figure()
#plt.scatter(t,dPhi)

print(str(max(dPhi)))

"""