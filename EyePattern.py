# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 15:27:40 2022

@author: 2175469R
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def EyeRead(path):
    data = pd.read_csv(path,header = 1)
    time = data.values[:,0]
    ch1 = data.values[:,1]
    ch2 = data.values[:,2]
    return time, ch1, ch2

path = r"D:\4NS04.CSV"

t,ch1,ch2 = EyeRead(path)
ch1 = ch1*1000
t = t*1e9
trigger = 0.6

interval = []
plt.figure()

for i in range(len(ch2)-1):    
    if ch2[i]<=0.6 and ch2[i+1]>0.6:
        interval.append(i)
        if len(interval)>2:
            tempT = t-t[interval[-2]]
            plt.scatter(tempT[interval[-3]:interval[-1]],ch1[interval[-3]:interval[-1]],c='b')
            
        
plt.title('Intensity modulator eye pattern at 7.8MBaud',size = 25)
plt.xlabel('Time(ns)',size = 25)
plt.ylabel('Voltage(mV)',size = 25)
plt.grid()
plt.tick_params(axis = 'both', direction = 'in',labelsize = 25,length = 10,width = 2,bottom=True, top=True, left=True, right=True)




