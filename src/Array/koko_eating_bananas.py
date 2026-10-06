"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""
from math import ceil

from src.res.Array.koko_eating_bananas import input as ip, output as op
from validator import are_two_arrays_same
from typing import List


def solve():
    """
    The solution of the program
    :return: None
    """
    input = ip.i_p
    results = []

    for inp in input:
        arr, k = inp
        results.append(binary_search(arr, k))
    print(results)

    if not are_two_arrays_same(results, op.o_p):
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def brute_force(nums: List[int], h: int) -> int:
    k = 1
    while True:
        hours = 0

        for pile in nums:
            hours += ceil(pile / k)

        if hours <= h:
            return k

        k += 1

def binary_search(piles: List[int], hrs: int) -> int:
    """
    This is a binary search problem. To show that, we can spread the range of k from 1 to max(piles).
    Then we have to find the first value which is fast enough. The searching makes it a BS problem.
    """
    l, h = 1, max(piles)

    while l < h:
        m = l + (h - l) // 2

        hours = 0
        for pile in piles:
            hours += ceil(pile/m)

        if hours <= hrs:
            h = m
        else:
            l = m + 1       

    return l 
