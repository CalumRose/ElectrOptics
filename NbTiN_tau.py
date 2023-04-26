# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 10:53:05 2022

@author: 2175469R
"""
import numpy as np
import matplotlib.pyplot as plt


nbTc = 8
nbnTc = 12
nbtinTc = 10
k = 1.38e-23


#t = 0.5*Tc
nbT = np.linspace(0.1,0.5,100)*nbTc
nbnT = np.linspace(0.1,0.5,100)*nbnTc
nbtinT = np.linspace(0.1,0.5,100)*nbtinTc

#tau0 = 5e-12
nbtau0 = 370e-12
nbntau0 = 60e-12
nbtintau0 = 100e-12


fig = plt.figure()

nbtauQP = 1/(np.pi**0.5/nbtau0*(2*1.76*k*nbTc/(k*nbTc))**2.5*(nbT/nbTc)**0.5*np.exp(-1.76*k*nbTc/(k*nbT)))
nbntauQP = 1/(np.pi**0.5/nbntau0*(2*1.76*k*nbnTc/(k*nbnTc))**2.5*(nbnT/nbnTc)**0.5*np.exp(-1.76*k*nbnTc/(k*nbnT)))
nbtintauQP = 1/(np.pi**0.5/nbtintau0*(2*1.76*k*nbtinTc/(k*nbtinTc))**2.5*(nbtinT/nbtinTc)**0.5*np.exp(-1.76*k*nbtinTc/(k*nbtinT)))

ax = fig.add_subplot(1,1,1)
ax.scatter(nbT/nbTc,nbtauQP,label = 'Nb $\u03C4_{QP}$')
ax.scatter(nbnT/nbnTc,nbntauQP,label = 'NbN $\u03C4_{QP}$')
ax.scatter(nbtinT/nbtinTc,nbtintauQP,label = 'NbTiN $\u03C4_{QP}$')
plt.title('Quasiparticle recombination time for different materials',size = 25)
plt.xlabel('Temperature $T/T_c$',size = 25)
plt.ylabel('$\u03C4_{QP}$ (s)',size = 25)
plt.tick_params(axis = 'both', direction = 'in',labelsize = 25,length = 10,width = 2,bottom=True, top=True, left=True, right=True)
ax.grid()


ax.legend(fontsize = 20)

ax.set_yscale('log')


#tauQP = 1/(np.pi**0.5/tau0*(2*D/(k*Tc))**2.5*(t/Tc)**0.5*np.exp(-D/(k*t)))


