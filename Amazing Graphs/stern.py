#!/usr/bin/env python3

"""
    stern.py
    Stern's sequence
    https://oeis.org/A002487
Stern's diatomic series (or Stern-Brocot sequence): a(0) = 0, a(1) = 1; for n > 0: a(2*n) = a(n), a(2*n+1) = a(n) + a(n+1).
"""


import matplotlib.pyplot as plt


def stern_flat(iterations=20):
    digits = [0, 1, 1, 2]
    last = [1, 2]

    for I in range(3, iterations):
        midsum = [x + y for x, y in zip(last, last[1:])] + [I]

        new_last = []
        for x, y in zip(last, midsum):
            new_last.extend([x, y])

        last = new_last
        digits.extend(new_last)

    return digits


stern = stern_flat(20)

fig, ax = plt.subplots(1)
ax.plot(stern, ".", markersize=0.1)
plt.show()
