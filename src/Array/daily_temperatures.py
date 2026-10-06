"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
"""
from src.res.Array.daily_temperatures import input as ip, output as op
from validator import are_two_arrays_same
from typing import List


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(stack_optimised(n))
    print(results)

    if not are_two_arrays_same(results, op.o_p):
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def brute_force(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    res = [0] * n

    for i in range(n):
        for j in range(i+1, n):
            if temperatures[j] > temperatures[i]:
                res[i] = j - i
                break

    return res


def stack_optimised(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    stack = []
    res = [0] * n

    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            previous_temp, previous_idx = stack.pop()
            res[previous_idx] = i - previous_idx

        stack.append((temp, i))

    return res
