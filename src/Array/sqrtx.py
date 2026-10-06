"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""
from src.res.Array.sqrtx import input as ip, output as op
from validator import are_two_arrays_same
from typing import List


def solve():
    """
    The solution of the program
    :return: None
    """
    input = ip.i_p
    results = []

    for x in input:
        results.append(linear(x))
    print(results)

    if not are_two_arrays_same(results, op.o_p):
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def binary_search(x: int) -> int:
    if x < 2:
        return x

    l, h = 0, x // 2

    while l <= h:
        m = l + (h - l) // 2
        square = m * m

        if square == x:
            return m
        elif square < x:
            l = m + 1
        else:
            h = m - 1

    return h


def linear(x: int) -> int:
    for i in range(x//2 + 1, -1, -1):
        if i * i == x:
            return i
        elif i * i < x:
            return i