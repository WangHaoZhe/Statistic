#!/usr/local/bin/python3.11
# -*- coding: UTF-8 -*-
# @Project : Statistic
# @File    : Problem2.py
# @Author  : Albert Wang
# @Time    : 2024/4/22
# @Brief   : None

import numpy as np
from matplotlib import pyplot as plt

count = []
result = []

for _ in range(1000000):
    random_sequence = np.random.randint(low=1, high=11, size=20)

    num = 0
    for i in range(1, 10 + 1):
        if i in random_sequence:
            num += 1
    count.append(num)

for i in range(10):
    result.append(count.count(i + 1))

x = np.linspace(1, 10, 10)
plt.xlabel("Number of stops")
plt.ylabel("Freq")
plt.xlim(1, 11)
plt.bar(x, result, color="#1f77b4")
plt.show()

print(sum(count) / len(count))
