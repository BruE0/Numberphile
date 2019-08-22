#!/usr/bin/env python3

"""
    remy.py
    Rémy Sigrist
    https://oeis.org/A279125
Lexicographically earliest sequence such that, for any distinct i and j, 
a(i)=a(j) implies (i AND j)=0 (where AND stands for the bitwise AND operator).

"""

from collections import defaultdict
import matplotlib.pyplot as plt


def remy(size=10_000):
    seq = [0]
    index_that_used_n = defaultdict(list)
    index_that_used_n.update({0: [1]})
    attempt = 0
    while len(seq) < size:
        index = len(seq) + 1
        if any(index & num for num in index_that_used_n[attempt]):
            attempt += 1
        else:
            seq.append(attempt)
            index_that_used_n[attempt].append(index)
            attempt = 0
    return seq


fig, ax = plt.subplots(1)

ax.plot(remy(10_000), ".", markersize=0.5)

plt.show()
