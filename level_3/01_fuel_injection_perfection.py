"""
Fuel Injection Perfection
=========================

Commander Lambda has asked for your help to refine the automatic
quantum antimatter fuel injection system for her LAMBCHOP doomsday
device. It's a great chance for you to get a closer look at the
LAMBCHOP - and maybe sneak in a bit of sabotage while you're at it -
so you took the job gladly.

Quantum antimatter fuel comes in small pellets, which is convenient
since the many moving parts of the LAMBCHOP each need to be fed fuel
one pellet at a time. However, minions dump pellets in bulk into the
fuel intake. You need to figure out the most efficient way to sort and
shift the pellets down to a single pellet at a time.

The fuel control mechanisms have three operations:

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the
destructive energy released when a quantum antimatter pellet is cut in
half, the safety controls will only allow this to happen if there is
an even number of pellets)

Write a function called answer(n) which takes a positive integer as a
string and returns the minimum number of operations needed to
transform the number of pellets to 1. The fuel intake control panel
can only display a number up to 309 digits long, so there won't ever
be more pellets than you can express in that many digits.

For example:
answer(4) returns 2: 4 -> 2 -> 1
answer(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1


Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) n = "4"
Output:
    (int) 2

Inputs:
    (string) n = "15"
Output:
    (int) 5
"""

import sys
sys.setrecursionlimit(2500)


cache = {1: 0}


def memoization(n):
    if n in cache:
        return cache[n]

    if n % 2 == 0:
        cache[n] = 1 + memoization(n/2)
    else:
        cache[n] = 1 + min(memoization(n+1), memoization(n-1))

    return cache[n]


def answer(n):
    # your code here
    return memoization(int(n))
