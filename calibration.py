import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv
import pandas as pd

pulseheights_A = [38.824, 80.446]
pulseheights_B = [18.905, 40.405]
energy = [511, 1274]

E_fit_A = []
E_fit_B = []
p_fit_A = []
p_fit_B = []

def convert(x, A, B):
    return A*x + B

constants_A = curve_fit(convert, pulseheights_A, energy, p0 = [0.01, -0.05])
constants_B = curve_fit(convert, pulseheights_B, energy, p0 = [0.01, -0.05])

A_A, A_B = constants_A[0]
B_A, B_B = constants_B[0]

print(A_A, A_B)
print(B_A, B_B)

for x in np.arange(20, 90, 0.01):
    E_A = convert(x, A_A, A_B)
    E_fit_A.append(E_A)
    p_fit_A.append(x)
  
for x in np.arange(10, 60, 0.01):
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