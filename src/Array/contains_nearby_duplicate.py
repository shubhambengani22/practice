"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

from src.res.Array.contains_nearby_duplicate import input as ip, output as op
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
        results.append(optimised(arr, k))
    print(results)

    if not are_two_arrays_same(results, op.o_p):
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def brute(nums: List[int], k: int) -> bool:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    for i in range(len(nums)-k):
        if freq.get(nums[i]) >= 2:
            j = i + k
        while j > i:
            if nums[j] == nums[i]:
                return True
            j -= 1
    return False


def optimised(nums: List[int], k: int) -> bool:
    dup = {}
    n = len(nums)

    for i in range(n):
        if nums[i] in dup and abs(dup[nums[i]] - i) <= k:
            return True
        dup[nums[i]] = i

    return False
