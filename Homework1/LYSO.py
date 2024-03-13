#!/usr/local/bin/python3.11
# -*- coding: UTF-8 -*-
# @Project : Statistic
# @File    : LYSO.py
# @Author  : Albert Wang
# @Time    : 2024/3/13
# @Brief   : None

import numpy as np

from matplotlib import pyplot as plt

reload = 5e4  # 0.1ms * 500M
data = np.loadtxt("LYSO_ttt.txt", int)  # Load file
count = []
tail = 0

# Calculate total num in each group
for i in range(data.shape[0]):
    if data[i] - data[tail] > reload:
        count.append(i - tail)
        tail = i
print(len(count))

# Plot count
plt.xlabel("Time (0.1ms)")
plt.ylabel("Number of signal generated")
plt.title("Lu176 Decay Count")
plt.bar(np.linspace(1, len(count), len(count)), np.array(count), color="#1f77b4", label="Count in each time section")
# Plot expection
plt.plot([0, len(count)], [3.279, 3.279], color="#ff7f0e", label="Expectation")

plt.legend()
plt.show()
