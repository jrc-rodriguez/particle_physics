# this is a program for calibration of experiment
# it determines the coefficients to transfer from pulseheight to energy so data can be adjusted to photon energy of 511 keV

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv
import pandas as pd

pulseheights_A = [196.85240963855424, 477.15361445783134]
pulseheights_B = [196.85240963855424, 477.15361445783134]
energy = [511, 1274]

E_fit_A = []
E_fit_B = []
p_fit_A = []
p_fit_B = []

def convert(x, A, B):
    return A*x + B

constants_A = curve_fit(convert, pulseheights_A, energy, p0 = [2.5, -25.5])
constants_B = curve_fit(convert, pulseheights_B, energy, p0 = [2.5, -30.8])

A_A, A_B = constants_A[0]
B_A, B_B = constants_B[0]

print(A_A, A_B)
print(B_A, B_B)

for x in np.arange(0, 560, 0.01):
    E_A = convert(x, A_A, A_B)
    E_fit_A.append(E_A)
    p_fit_A.append(x)
  
for x in np.arange(0, 560, 0.01):
    E_B = convert(x, B_A, B_B)
    E_fit_B.append(E_B)
    p_fit_B.append(x)
    
plt.plot(p_fit_A, E_fit_A, label = 'best fit', color = 'red')
plt.plot(pulseheights_A, energy, 'o', markersize = 3, label = 'experiment')
plt.xlabel("pulseheights for CS (mv)")
plt.ylabel("Energy for CS (KeV)")
plt.legend(loc = 'upper left')
plt.show()

plt.plot(p_fit_B, E_fit_B, label = 'best fit', color = 'red')
plt.plot(pulseheights_B, energy, 'o', markersize = 3, label = 'experiment')
plt.xlabel("pulseheights for CS (mv)")
plt.ylabel("Energy for CS (KeV)")
plt.legend(loc = 'upper left')
plt.show()