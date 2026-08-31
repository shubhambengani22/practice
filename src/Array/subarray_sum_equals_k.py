"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""
from src.res.Array.subarray_sum_equals_k import input as ip, output as op
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
        results.append(optimised_prefix_sum(arr, k))
    print(results)

    if not are_two_arrays_same(results, op.o_p):
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def brute_force(nums: List[int], k: int) -> int:
    """
    Find all possible subarrays and compare their sum against k
    """
    n = len(nums)
    count = 0

    for i in range(n):
        for j in range(i+1, n+1):
            arr = nums[i:j]
            if sum(arr) == k:
                count += 1

    return count


def optimised_brute_force(nums: List[int], k: int) -> int:
    """
    Removing sum recomputation and complexity reduced to n^2
    """
    n = len(nums)
    count = 0

    for i in range(n):
        subarray_sum = 0
        for j in range(i, n):
            subarray_sum += nums[j]
            if subarray_sum == k:
                count += 1
    return count


def prefix_sum(nums: List[int], k: int) -> int:
    n = len(nums)
    prefix_sums = [0] * n
    prefix_sums[0] = nums[0]
    count = 0

    for i in range(n):
        if i > 0:
            prefix_sums[i] = prefix_sums[i-1] + nums[i]
        if prefix_sums[i] == k:
            count += 1
        for j in range(i, n):
            if prefix_sums[i] - prefix_sums[j] == k:
                count += 1

    return count


def optimised_prefix_sum(nums: List[int], k: int) -> int:
    n = len(nums)
    prefix_sums = [0] * n
    prefix_sums[0] = nums[0]
    count = 0
    seen = {0: 1}

    for i in range(n):
        if i > 0:
            prefix_sums[i] = prefix_sums[i-1] + nums[i]
        needed = prefix_sums[i] - k
        count += seen.get(needed, 0)
        seen[prefix_sums[i]] = seen.get(prefix_sums[i], 0) + 1

    return count