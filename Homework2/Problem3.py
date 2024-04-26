#!/usr/local/bin/python3.11
# -*- coding: UTF-8 -*-
# @Project : Statistic
# @File    : Problem3.py
# @Author  : Albert Wang
# @Time    : 2024/4/22
# @Brief   : None

import matplotlib.pyplot as plt
import numpy as np

# n = [1, 10, 30, 60]
# attempt = 100000000
# Result: [109.997606, 259.38078296321333, 1753.8927671964461, 26830.639793920483]

n = [1, 10, 30, 60, 90, 180, 360]
attempt = 1000000
price = []
price_less_than_one_prob = []
price_less_than_one_std = []

for i in n:
    price_n = np.full(attempt, 100.0)
    for j in range(i):
        random_sequence = np.random.choice([1.7, 0.5], size=attempt)
        price_n *= random_sequence
        print(i, j)
    price.append(np.mean(price_n))
    p_ = np.sum(price_n < 1) / attempt
    price_less_than_one_prob.append(p_)
    price_less_than_one_std.append(1.96 * np.sqrt(p_ * (1 - p_)) / attempt)

plt.errorbar(
    n,
    price_less_than_one_prob,
    yerr=price_less_than_one_std,
    fmt="o",
    color="blue",
    ecolor="red",
    capsize=5,
)
plt.xlabel("n")
plt.ylabel("P")
plt.title("Probability of Xn less than 1")
plt.show()
