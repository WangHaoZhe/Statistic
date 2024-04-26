#!/usr/local/bin/python3.11
# -*- coding: UTF-8 -*-
# @Project : Statistic
# @File    : Problem1.py
# @Author  : Albert Wang
# @Time    : 2024/4/22
# @Brief   : None

import numpy as np
from matplotlib import pyplot as plt


def calculate_diff(array_, lower_limit_, upper_limit_, step_):
    len_ = int((upper_limit_ - lower_limit_) / step_)
    t_ = np.linspace(lower_limit_ + step_, upper_limit_, len_)
    diff_ = np.diff(array_, axis=0)
    diff_.sort()
    n_ = np.zeros(len_)
    # Calculate the distribution
    i, j = 0, 0
    last_j = 0
    while i < t_.shape[0] and j < diff_.shape[0]:
        if diff_[j] < lower_limit_ + (i + 1) * step_:
            j += 1
            if diff_[j - 1] < lower_limit_ + i * step_:
                last_j = j
        else:
            n_[i] = j - last_j
            i += 1
            last_j = j
    return t_, n_


# Question 1 Begin
lambda_1 = 100
lambda_2 = 200
total_time = 36000
tau = 1e-5

# Generate event time series
events_1 = np.random.exponential(1 / lambda_1, total_time * lambda_1)
events_2 = np.random.exponential(1 / lambda_2, total_time * lambda_2)

# Convert event series to time series
time_series_1 = np.cumsum(events_1)
time_series_2 = np.cumsum(events_2)

# Plot histogram
t, n = calculate_diff(time_series_1, 0.000, 0.100, 1e-3)  # 1-100ms
plt.xlabel("Time (ms)")
plt.ylabel("Number")
plt.title("Time difference distribution of 1st phototube")
plt.bar(t * 1e3, n, color="#1f77b4")
plt.show()
# Question 1 End

# Question 2 Begin
event_a = []
i, j = 0, 0
while i < time_series_1.shape[0] and j < time_series_2.shape[0]:
    time_diff_ = abs(time_series_1[i] - time_series_2[j])
    if time_diff_ <= tau:
        event_a.append(min(time_series_1[i], time_series_2[j]))
    if time_series_1[i] < time_series_2[j]:
        i += 1
    else:
        j += 1
    print(i, j, time_diff_)
# Question 2 End

# Question 3 Begin
t_a, n_a = calculate_diff(event_a, 1, 20, 1)
plt.xlabel("Time (s)")
plt.ylabel("Number")
plt.title("Time difference distribution of A")
plt.bar(t_a, n_a, color="#1f77b4")
plt.show()
# Question 3 End

# Question 4 Begin
print("Event A number: ", len(event_a))
# Question 4 End
