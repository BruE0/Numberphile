#!/usr/bin/env python3
# wisteria.py


import numpy as np
import matplotlib.pyplot as plt
from functools import reduce


def wisteria(num):
    non_zero_digits = [int(x) for x in str(num) if x != '0']
    if num == 0:
        return 0
    return num - reduce(lambda x, y: x*y, non_zero_digits)



fig, ax = plt.subplots(1)

X = np.arange(100000)

wisteriavector = np.vectorize(wisteria)
ax.plot(X, wisteriavector(X), ".", markersize=0.2)

ax.minorticks_on()
ax.grid(True, which="both")
plt.show()
