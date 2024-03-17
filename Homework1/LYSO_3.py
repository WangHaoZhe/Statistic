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

count = {}

# Calculate total num in each group (1us~200us, step=1us)
for i in range(200):
    for j in range(len(diff)):
        if i < diff[j] < i + 1:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

sorted_count = dict(sorted(count.items()))
x_ = list(sorted_count.keys())
n_ = list(sorted_count.values())
print(x_)
print(n_)

# Plot histogram
plt.xlabel("Time (us)")
plt.ylabel("Number")
plt.title("Time difference distribution of Lu176 decay")
plt.bar(x_, n_, color="#1f77b4")
plt.show()
