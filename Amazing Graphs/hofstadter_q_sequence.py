#!/usr/bin/env python3

"""
    hofstadter_q_sequence.py
    Hofstadter's Q Sequence
    https://oeis.org/A005185
Hofstadter Q-sequence: a(1) = a(2) = 1; a(n) = a(n-a(n-1)) + a(n-a(n-2)) for n > 2. 
"""


import matplotlib.pyplot as plt


def hofstadter(iterations=10_000):
    seq = [1, 1]
    for I in range(3, iterations + 3):
        steps1 = seq[-seq[-1]]
        steps2 = seq[-seq[-2]]
        seq.append(steps1 + steps2)
    return seq


fig, ax = plt.subplots(1)

ax.plot(hofstadter(100_000), ".", markersize=0.1)

plt.show()
