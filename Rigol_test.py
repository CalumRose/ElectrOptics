# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:50:04 2023

@author: 2175469R
"""

import pyvisa as visa


rm = visa.ResourceManager()
print(rm.list_resources())

inst = rm.open_resource('USBInstrument3')
#inst.timeout  = 10000
print(inst.query("*IDN?"))

a = inst.query(':SOUR:LEV?')
inst.write(':SOUR:LEV -80')
#USB0::0x1AB1::0x0992::DSG3A183600072::0::INSTR