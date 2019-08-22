#!/usr/bin/env python3

"""
    balanced_ternary.py
    2019.08
"""

import matplotlib.pyplot as plt
import numpy as np


def ternary(integer):
    """integer in base 3"""
    digits = []
    while integer > 0:
        digits.append(str(integer % 3))
        integer //= 3
    return "".join(digits[::-1]) if digits else "0"


def baln(n):
    nlist = ["-1" if x == "2" else x for x in ternary(n)]

    answer, base = 0, 0
    for n in reversed(nlist):
        answer += int(n) * 3 ** base
        base += 1
    return answer


fig, ax = plt.subplots(1)

X = np.arange(50000)

balnvector = np.vectorize(baln)
ax.plot(X, balnvector(X), ".", markersize=1)

ax.minorticks_on()
ax.axis("square")
ax.grid(True, which="both")
plt.show()
