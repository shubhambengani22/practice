"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""
from src.res.Array.search_insert_position import input as ip, output as op
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
        results.append(with_binary_search(arr, k))
    print(results)

    if not are_two_arrays_same(results, op.o_p):
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def with_binary_search(nums: List[int], k: int) -> int:
    n = len(nums)
    l, h = 0, n - 1

    while l <= h:
        m = l + (h - l) // 2

        if nums[m] == k:
            return m
        elif nums[m] < k:
            l = m + 1
        else:
            h = m - 1

    print(l, h)

    return l
