import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv


pulseheights_CS = [21.8, 59, 70]
energy_CS = [0.04615, 0.5461, 0.6612]
E_fit_CS = []
P_fit_CS = []
E_err_CS = []
P_err = 0.5
P_err_list_CS = []

pulseheights_NA = [54.5, 131.5]
energy_NA = [0.511, 1.274]
E_fit_NA = []
P_fit_NA = []
E_err_NA = []
P_err_list_NA = []

def convert(x, A, B):
    return A*x + B

def error(a, p, c, a_err, p_err, c_err):
  return ((p * a_err) **2 + (a * p_err) **2 + c_err ** 2) ** 0.5

constants_CS = curve_fit(convert, pulseheights_CS, energy_CS, p0 = [0.01, -0.05])
constants_NA = curve_fit(convert, pulseheights_NA, energy_NA, p0 = [0.01, -0.05])

A_CS, B_CS = constants_CS[0]
A_err_CS = constants_CS[1][0][0]
B_err_CS = constants_CS[1][0][1]

A_NA, B_NA = constants_NA[0]
A_err_NA = constants_NA[1][0][0]
B_err_NA = constants_NA[1][0][1]

#print(A_CS, B_CS)
#print(A_err_CS, B_err_CS)
print(constants_NA)

print(A_NA, B_NA)
print(A_err_NA, B_err_NA)

for p in pulseheights_NA:
  E_err_NA_value = error(A_NA, p, B_NA, A_err_NA, P_err, B_err_NA)
  E_err_NA.append(E_err_NA_value)
  P_err_list_NA.append(P_err)

for p in pulseheights_CS:
  E_err_CS_value = error(A_CS, p, B_CS, A_err_CS, P_err, B_err_CS)
  E_err_CS.append(E_err_CS_value)
  P_err_list_CS.append(P_err)

for x in np.arange(15, 80, 0.01):
    E_CS = convert(x, A_CS, B_CS)
    E_fit_CS.append(E_CS)
    P_fit_CS.append(x)
  
for x in np.arange(50, 150, 0.01):
    E_NA = convert(x, A_CS, B_CS)
    E_fit_NA.append(E_NA)
    P_fit_NA.append(x)

plt.errorbar(pulseheights_CS, energy_CS,  yerr = E_err_CS, xerr = P_err_list_CS, fmt = '.', label = 'experiment')
plt.plot(P_fit_CS, E_fit_CS, label = 'best fit', color = 'red')
plt.xlabel("pulseheights for CS (mv)")
plt.ylabel("Energy for CS (KeV)")
plt.legend(loc = 'upper left')
plt.show()

plt.errorbar(pulseheights_NA, energy_NA,  yerr = E_err_NA, xerr = P_err_list_NA, fmt = '.', label = 'experiment')
plt.plot(P_fit_NA, E_fit_NA, label = 'best fit', color = 'red')
plt.xlabel("pulseheights for NA (mv)")
plt.ylabel("Energy for NA (KeV)")
plt.legend(loc = 'upper left')
plt.show()

def functie(a, x, b):
  return -a*x**2 + b

step = 0
test = []
test_x = []
for x in np.arange(-100, 100, 0.1):
  y = functie(50, x, 1485)
  test.append(y)
  test_x.append(x)

plt.plot(test_x, test)
plt.xlim(-50, 50)
plt.show()