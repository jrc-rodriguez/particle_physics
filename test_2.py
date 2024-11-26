import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_no_source = pd.read_csv("spectrum_no_source.csv")
pulseheights_no_source = data_no_source["pulseheight"]
counts_no_source_A = data_no_source["counts_ch_A"]
counts_no_source_B = data_no_source["counts_ch_B"]

x = []
y = []
for p, N in zip(pulseheights_no_source, counts_no_source_A):
    x.append(p)
    y.append(N)

    plt.clf()
    plt.plot(x, y)
    plt.draw()
    plt.pause(0.001)