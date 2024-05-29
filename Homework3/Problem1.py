#!/usr/local/bin/python3.11
# -*- coding: UTF-8 -*-
# @Project : Statistic
# @File    : Problem1.py
# @Author  : Albert Wang
# @Time    : 2024/5/27
# @Brief   : None

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

c_inv = sp.integrate.quad(lambda x: x ** (-4.5), 100, 180)[0]

ns = [48, 462, 704, 594, 11, 11, 35]
nb = [1520, 66180, 201599, 257028, 123, 382, 2238]
sigma = [1.4, 1.5, 2.0, 2.7, 1.6, 1.6, 1.7]


def pdfb(x_):
    return 1 / c_inv * x_ ** (-4.5)


def pdfs(x_, mu_, sigma_):
    return 1 / (sigma_ * np.sqrt(2 * np.pi)) * np.exp(-((x_ - mu_) ** 2) / (2 * sigma_ ** 2))


def lnL(mu_, data_, ns_, nb_, sigma_):
    y_ = 0
    for i in range(len(data_)):
        y_ += np.log(
            ns_ / (ns_ + nb_) * pdfs(data_[i], mu_, sigma_)
            + nb_ / (ns_ + nb_) * pdfb(data_[i])
        )
    return y_


def scan(data_, ns_, nb_, sigma_):
    mu_ = np.linspace(120, 130, 10000)
    lnL_mu_ = lnL(mu_, data_, ns_, nb_, sigma_)

    mu_hat_ = mu_[np.argmax(lnL_mu_)]
    lnL_mu_hat_ = lnL_mu_[np.argmax(lnL_mu_)]

    start_, end_ = 0, 0
    for i_ in range(10000 - 1):
        if 2 * (lnL_mu_hat_ - lnL_mu_[i_]) > 1 > 2 * (lnL_mu_hat_ - lnL_mu_[i_ + 1]):
            start_ = mu_[i_]
        elif 2 * (lnL_mu_hat_ - lnL_mu_[i_]) < 1 < 2 * (lnL_mu_hat_ - lnL_mu_[i_ + 1]):
            end_ = mu_[i_]

    return mu_hat_, start_, end_


mu = np.linspace(100, 180, 1000)
lnLz_mu = np.zeros(1000)
for j in range(7):
    data = np.loadtxt("./mggdata20240513/mgg_cms2020_cat" + str(j) + ".txt")
    lnL_mu = lnL(mu, data, ns[j], nb[j], sigma[j])
    mu_hat, start, end = scan(data, ns[j], nb[j], sigma[j])
    lnL_mu_hat = lnL(mu_hat, data, ns[j], nb[j], sigma[j])
    print("category: ", j, "mu_hat: ", mu_hat, "68.3% CLlength", end - start)

    plt.plot(mu, 2 * (lnL_mu_hat - lnL_mu))
    plt.xlabel("mu")
    plt.ylabel("2 * (L_mu_hat - L)")
    plt.xlim(123, 130)
    plt.ylim(0, 4.5)
    plt.title("category: " + str(j))
    plt.show()

    lnLz_mu = np.add(lnLz_mu, lnL_mu)


plt.plot(mu, lnLz_mu)
mu_hat = mu[np.argmax(lnLz_mu)]
lnLz_mu_hat = lnLz_mu[np.argmax(lnLz_mu)]
start, end = 0, 0
for i in range(1000 - 1):
    if 2 * (lnLz_mu_hat - lnLz_mu[i]) > 1 > 2 * (lnLz_mu_hat - lnLz_mu[i + 1]):
        start = mu[i]
    elif 2 * (lnLz_mu_hat - lnLz_mu[i]) < 1 < 2 * (lnLz_mu_hat - lnLz_mu[i + 1]):
        end = mu[i]
print("category: Lz", "mu_hat: ", mu[np.argmax(lnLz_mu)], "68.3% CLlength", end - start)

plt.plot(mu, 2 * (lnLz_mu_hat - lnLz_mu))
plt.xlabel("mu")
plt.ylabel("2 * (L_mu_hat - L)")
plt.xlim(123, 130)
plt.ylim(0, 4.5)
plt.title("category: Lz")
plt.show()
