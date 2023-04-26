# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:09:29 2022

@author: 2175469R
"""
import qkit
import scipy.optimize as opt
import numpy as np
import time
import matplotlib.pyplot as plt
import pandas as pd
import statistics as stat
import math

start_time = time.time()


def powerVtemp(powersCSV,tempsCSV):
    cooldownDF = pd.read_csv(tempsCSV)
    esaDF = pd.read_csv(powersCSV)
    
    powers = np.array(df.values[:,2])
    temps = cooldownDF.values[:,4]
    utcTimes = cooldownDF.values[:,0]
    times = df.values[:,1]
    
    corellatedT = []
    
    for time in times:
        closestInd = utcTimes.index(min(utcTimes, key=lambda x:abs(x-time)))
        corellatedT.append(temps[closestInd])
    
def writeCSV(d,path):
    df = pd.DataFrame(data = d)
    
    df.to_csv(path)

def readCSV(path):
    df = pd.read_csv(path)
    times = df.values[:,1]
    powers = np.array(df.values[:,2])
    fwhms = df.values[:,3]
    peaks = df.values[:,4]
    
    #powers = [10*math.log(x,10)+30 for x in powers]

    
    plt.figure()
    plt.scatter(times,peaks)
    plt.title('Peak wavelength')
    plt.xlabel('Time(s)')
    plt.ylabel('Wavelength(nm)')
    plt.grid()
    
    plt.figure()
    plt.scatter(times,fwhms)
    plt.title('FWHM')
    plt.xlabel('Time(s)')
    plt.ylabel('FWHM(nm)')
    plt.grid()
    
    plt.figure()
    plt.scatter(times,powers)
    plt.title('Power')
    plt.xlabel('Time(s)')
    plt.ylabel('Power(dBm)')
    plt.grid()
    
    return times,powers,fwhms,peaks
    
def Gaussian(freqRange,p,f,fwhm):
    
    stdev = fwhm/(2*np.sqrt(2*np.log(2)))
    
    power = []
    
    for i in freqRange:
        power.append(p*np.exp(-((i-f)**2/(2*(stdev)**2))))
    return np.array(power)

def advGaussFit(freq,traceLin,initials):
    params, cov = opt.curve_fit(Gaussian,freq,traceLin,p0 = initials)
    out = Gaussian(freq,params[0],params[1],params[2])
   
    return params[0],params[1],params[2]
    
def basicGaussFit(frequency, signal):
    peak = max(signal)
    peakInd = signal.argmax()
    peakF = frequency[peakInd]
    

    
    #plt.scatter(frequency,signal)
    
    for x in range(len(signal)):
        if x > peakInd:
            if signal[x] < 0.5*signal[peakInd]:
                m = (signal[x]-signal[x-1])/(frequency[x]-frequency[x-1])
                c = signal[x]-m*frequency[x]
                half = (signal[x]-c)/m
                fwhm = 2*(half-peakF)
                return peak,peakF,fwhm
            

    

sweep_time = 0.5
measurements = 100

qkit.cfg['load_visa'] = True
qkit.start()
ESA = qkit.instruments.create('ESA','Anritsu_MS2830A',address='USB0::0x0B5B::0x0006::6201585505::0::INSTR')

ESA.do_set_centerfreq(5e9)
ESA.do_set_freqspan(2e7)
powers = []
peaks = []
fwhms = []
times = []
reference = []
initials = np.array([1.5e-9,5e9,2e5])
plt.figure()
for i in range(measurements):
    freq = ESA.get_frequencies()
    trace = ESA.get_trace(1)
    trace = np.array(trace)
    traceLin = 10**(trace/10)/1000
    reference.append(trace[0])
    #plt.figure()
    plt.plot(freq,traceLin)
    
    #p,f,fwhm = basicGaussFit(freq,traceLin)
    #btraceFit = Gaussian(freq,p,f,fwhm)
    #plt.plot(freq,btraceFit)
    
    p,f,fwhm = advGaussFit(freq,traceLin,initials)
    #p = 0
    #f = 0
    #fwhm = 0
    atraceFit = Gaussian(freq,p,f,fwhm)
    plt.plot(freq,atraceFit)
    
    #plt.figure()
    #plt.scatter(freq,traceLin-btraceFit)
    #plt.scatter(freq,traceLin-atraceFit)
    
    #p = 10*math.log(p,10)+30
    powers.append(p)
    peaks.append(f)
    fwhms.append(fwhm)
    times.append(time.time())
    initials = [p,f,fwhm]
    print('Completed ' + str(i) + ' of ' + str(measurements) + ' measurements' )
    if i % 2 == 0:
        csvData = pd.DataFrame({'Frequency': freq, 'Power': trace})
        folder = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\Cold_PD\traceDataWarmup/"
        path = folder + str(round(time.time())) + '.csv'
        writeCSV(csvData,path)
    #time.sleep(300)

powerVar = stat.variance(powers)
peakVar = stat.variance(peaks)
fwhmVar = stat.variance(fwhms)



path = r"C:\Users\2175469R\OneDrive - University of Glasgow\Documents\PhD stuff\ElectroOptic\Data\Anritsu\LongRuns\NewData\mod_5G_10db_n100_BW20M.csv"
df = pd.DataFrame({'Time': times, 'Power': powers, 'fwhm': fwhms, 'Frequency': peaks})
writeCSV(df,path)




plt.figure()
plt.scatter(times,peaks)
plt.title('Peak wavelength, variance = %f' %peakVar)
plt.xlabel('Time(s)')
plt.ylabel('Wavelength(nm)')
plt.grid()

plt.figure()
plt.scatter(times,fwhms)
plt.title('FWHM, variance = %f' %fwhmVar)
plt.xlabel('Time(s)')
plt.ylabel('FWHM(nm)')
plt.grid()

plt.figure()
plt.scatter(times,powers)
#plt.scatter(times,reference)
plt.title('Power, variance = %f' %powerVar)
plt.xlabel('Time(s)')
plt.ylabel('Power(mW)')
plt.grid()