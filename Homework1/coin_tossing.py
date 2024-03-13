#!/usr/local/bin/python3.11
# -*- coding: UTF-8 -*-
# @Project : Statistic
# @File    : coin_tossing.py
# @Author  : Albert Wang
# @Time    : 2024/3/13
# @Brief   : None

import random

from matplotlib import pyplot as plt

attempt = 10000000
total_try = 0
log_table = {}

for i in range(attempt):
    temp = [2, 2, 2]
    this_try = 0
    while temp != [1, 0, 1]:
        # Shift temp
        temp[0] = temp[1]
        temp[1] = temp[2]
        temp[2] = random.randint(0, 1)
        this_try += 1

    total_try += this_try

    # Add data into log_table
    if this_try in log_table:
        log_table[this_try] += 1
    else:
        log_table[this_try] = 1

# Calculate the average try
average_try = total_try / attempt
print(average_try)

# Sort the log_table from min to max
sorted_log = dict(sorted(log_table.items()))
x_ = list(sorted_log.keys())
n_ = list(sorted_log.values())
print(x_)
print(n_)

# Plot histogram
plt.xlabel("Number of coins")
plt.ylabel("Number of times")
plt.title("Coin Tossing (Head-Tail-Head)")
plt.bar(x_, n_, color="#1f77b4", label="Number of times")
plt.show()

# Calculate the possibility of at least 50 tries
in_fifty = 0
for i in range(50):
    if i in log_table:
        in_fifty += log_table[i]
print((attempt - in_fifty) / attempt)

# hth: 10.0005984 0.003
# htt: 7.998652   5.68e-05
