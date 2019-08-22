#!/usr/bin/env python3
"""
    prime_minus_binary_reversal.py
    2019.08
    https://oeis.org/A265326
n-th prime minus its binary reversal.
"""

import numpy as np
import matplotlib.pyplot as plt


def sieve(n):
    """ Sieve of Erathostenes up to n"""
    primes = np.ones(n, dtype=bool)
    primes[0:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i :: i] = False
    return np.nonzero(primes)[0]


def prime_minus_binary_reversal(num):
    binary_reversed = f"{num:b}"[::-1]
    return num - int(binary_reversed, 2)



fig, ax = plt.subplots(1)

primes = sieve(1000000)
reversal = np.vectorize(prime_minus_binary_reversal)

ax.plot(primes, reversal(primes), ".", markersize=0.5)

ax.minorticks_on()
ax.grid(True, which="both")
plt.show()
