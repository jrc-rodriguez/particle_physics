import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv
import pandas as pd

# adds counts
def add_counts(dataset_1, dataset_2):
    total_counts = []
    
    for i, j in zip(dataset_1, dataset_2):
        total_counts.append(i + j)
        
    return total_counts

# cuts data 
def adjust(dataset_1, dataset_2):
    x_data = []
    y_data = []
    
    for i, j in zip(dataset_1, dataset_2):
        if i > 180 and i < 240:
            x_data.append(i)
            y_data.append(j)
            
    return x_data, y_data

# cuts data but for energy
def adjust_energy(dataset_1, dataset_2):
    x_data = []
    y_data = []
    
    for i, j in zip(dataset_1, dataset_2):
        if i > 500 and i < 520:
            x_data.append(i)
            y_data.append(j)
            
    return x_data, y_data

# energy conversion for channel A and B
def energy_A(dataset):
    data = []
    a = 18.33165153044063
    b = -200.70803901782693
    for p in dataset:
        E = a * p + b
        data.append(E)
        
    return data

def energy_B(dataset):
    data = []
    a = -51.330350835884154
    b = 1481.40028255239
    for p in dataset:
        E = a * p + b
        data.append(E)
        
    return data

# removes background radiation
def remove_background(dataset, dataset_2):
    data = []
    
    for i, j in zip(dataset, dataset_2):
        x = i - j
        data.append(x)
    
    return data