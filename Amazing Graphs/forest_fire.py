#!/usr/bin/env python3

"""
    forest_fire.py
    2019.08
    https://oeis.org/A229037
Sequence of positive integers where each is chosen 
to be as small as possible subject to the condition that 
no three terms a(j), a(j+k), a(j+2k) (for any j and k) 
form an arithmetic progression.

It takes too long for a large number of points.
"""

import matplotlib.pyplot as plt


NO_POINTS = 2000


def three_points_same_distance(lst):
    X = len(lst) - 1
    Y = lst[-1]
    for idx, y in enumerate(lst[-2:len(lst)//2-1:-1], 2):
        x = len(lst) - idx
        if (2*y - Y) == lst[2*x - X]:
            return True
    return False


def forest_fire(size):
    nums = [1, 1]
    while len(nums) < size:
        attempt = 1
        while True:
            nums.append(attempt)
            if three_points_same_distance(nums):
                nums.pop()
                attempt += 1
            else:
                break
    return nums


burntforest = forest_fire(NO_POINTS)

fig, ax = plt.subplots(1)

ax.plot(burntforest, ".")
ax.minorticks_on()
ax.grid(True, which="both")
plt.show()
