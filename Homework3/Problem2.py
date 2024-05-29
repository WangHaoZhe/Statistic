#!/usr/local/bin/python3.11
# -*- coding: UTF-8 -*-
# @Project : Statistic
# @File    : Problem2.py
# @Author  : Albert Wang
# @Time    : 2024/5/28
# @Brief   : None

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as special


def coverage_prob(s_, method):
    b_ = 3.2
    n_ = np.random.poisson(s_ + b_, 1000000)
    s_up_ = 0
    if method == "classical":
        s_up_ = 0.5 * special.chdtri(2 * (n_ + 1), 0.1) - b_
    elif method == "bayesian":
        s_up_ = 0.5 * special.chdtri(2 * (n_ + 1), 0.1 * (special.chdtrc(2 * (n_ + 1), 2 * b_))) - b_
    p_ = np.count_nonzero(s_up_ > s_) / 1000000
    return p_


p_classical = np.array([])
p_bayesian = np.array([])
s = np.linspace(0.1, 20, 200)
for i in s:
    p_classical = np.append(p_classical, coverage_prob(i, method="classical"))
    p_bayesian = np.append(p_bayesian, coverage_prob(i, method="bayesian"))

plt.plot(s, p_classical, color="#1f77b4", label="Classical")
plt.plot(s, p_bayesian, color="#ff7f0e", label="Bayesian")
plt.xlabel("s")
plt.ylabel("p")
plt.title("Coverage probability of 90% confidence interval for s")
plt.legend()
plt.show()
