#!/usr/bin/env python3

"""
    hofstadter_conway_cousin.py
    A chaotic cousin of the Hofstadter-Conway sequence
    https://oeis.org/A055748
a(1) = 1, a(2) = 1, a(n) = a(a(n-1)) + a(n - a(n-2) - 1) for n >= 3.

"""


import matplotlib.pyplot as plt


def hofstadter_cousin(iterations=10_000):
    seq = [1, 1]
    for I in range(3, iterations + 3):
        steps1 = seq[seq[-1]-1]
        steps2 = seq[-seq[-2]-1]
        seq.append(steps1 + steps2)
    return seq


fig, ax = plt.subplots(1)

ax.plot(hofstadter_cousin(100_000), ".", markersize=0.1)

plt.show()
