# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 13:29:58 2023

@author: 2175469R
"""

import qkit



qkit.cfg['load_visa'] = True
qkit.start()
Rigol = qkit.instruments.create('Rigol','Rigol_DSG3060',address='USB0::0x1AB1::0x0992::DSG3A183600072::0::INSTR')
