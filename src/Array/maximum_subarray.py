"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""
from src.res.Array.maximum_subarray import input as ip, output as op
from validator import are_two_arrays_same
from typing import List


def solve():
    """
    The solution of the program
    :return: None
    """
    input = ip.i_p
    results = []

    for arr in input:
        results.append(maximum_subarray(arr))
    print(results)

    if not are_two_arrays_same(results, op.o_p):
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def maximum_subarray_brute_force(nums: List[int]) -> int:
    """
    Comparing all possible subarrays
    Args:
            Array of integers
        Returns:
            Maximum sum of the subarray
    """
    n = len(nums)
    max_sum = nums[0]

    for i in range(n):
        for j in range(i, n):
            max_sum = max(max_sum, sum(nums[i:j+1]))

    return max_sum


def maximum_subarray(nums: List[int]) -> int:
    n = len(nums)
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, n):
        current_sum = max(nums[i], nums[i] + current_sum)
        max_sum = max(max_sum, current_sum)

    return max_sum
