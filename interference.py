# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 11:38:09 2022

@author: 2175469R
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5*np.pi,2000)


phi = np.linspace(0,2*np.pi,100)
a = 1/np.sqrt(2)*np.sin(x)

outP = []

for p in phi:
    b = 1/np.sqrt(2)*np.sin(x+p)
    
    out = (a+b)**2
    
    aI = a**2
    aP = sum(aI)/1000
    
    outP.append(sum(out)/1000)


plt.figure()
plt.plot(phi,outP)

print(str(aP))
print(str(outP))