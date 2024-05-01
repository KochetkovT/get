import numpy as np
import pandas as pd
from textwrap import wrap
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D, HandlerTuple
from matplotlib.ticker import *

with open("settings.txt", 'r') as settings:
    freq, step = map(float, settings.read().split("\n"))

data = np.loadtxt("data.txt", dtype=int)

U_arr = data*step
time_charge = len(data)/freq
time_arr = np.arange(0, time_charge, 1/freq)

fig = plt.figure(figsize=(5*np.sqrt(2), 5), dpi=180)

ax1 = fig.add_subplot(111)
ax1.set_title("\n".join(wrap('Процесс заряда конденсатора в RC-цепочке', 60)), loc = 'center', fontsize=16)
ax1.plot(time_arr, U_arr, color = 'b', label="V(t)", markevery=range(0, len(data), 10), marker = "o")

ax1.set_xlabel("Время, с", fontsize = 10)
ax1.set_ylabel("Напряжение, В", fontsize = 10)

box = dict(
    boxstyle="square, pad=0.3", 
    ec="k",
    fc="w",
    ls="-",
    lw=1   
)

ax1.text(4, 1, "Время зарядки конденсатора {:.2f} c".format(time_charge), bbox = box, fontsize=10)

ax1.set_xlim(0)
ax1.set_ylim(0)
    
ax1.xaxis.set_minor_locator(AutoMinorLocator(10))
ax1.yaxis.set_minor_locator(AutoMinorLocator(10))

ax1.minorticks_on()

ax1.set_axisbelow(True)

# # ax1.grid(alpha = 0.5)
ax1.grid(which='major', linewidth=0.7, alpha = 0.7)
ax1.grid(which='minor', linestyle=':', linewidth=0.5, alpha = 0.7)

ax1.yaxis.set_label_coords(-0.1, 0.5) #custom positioning
ax1.legend()

plt.show()

fig.savefig("plot.svg")
fig.savefig("plot.png")

