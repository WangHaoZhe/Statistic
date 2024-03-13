#!/usr/local/bin/python3.11
# -*- coding: UTF-8 -*-
# @Project : Statistic
# @File    : LYSO_3.py
# @Author  : Albert Wang
# @Time    : 2024/3/13
# @Brief   : None

import numpy as np

from matplotlib import pyplot as plt

data = np.loadtxt("LYSO_ttt.txt", int)  # Load file

# Calculate the time difference
diff = []
for i in range(int(np.shape(data)[0]) - 1):
    diff.append(0.002 * np.array(data[i + 1] - data[i]))

# Plot histogram
plt.bar(np.linspace(1, len(diff), len(diff)), np.array(diff))
plt.ylabel("Time difference of signal generated (us)")
plt.title("Lu176 Decay Time Difference")
plt.show()
