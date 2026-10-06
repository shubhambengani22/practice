"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""
from src.res.Array.search_in_sorted_rotated_array import input as ip, output as op
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
        results.append(single_binary_search(arr, k))
    print(results)

    if not are_two_arrays_same(results, op.o_p):
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def find_pivot(nums: List[int]) -> int:
    n = len(nums)
    l, h = 0, n - 1

    while l < h:
        m = l + (h - l) // 2
        if nums[m] > nums[h]:
            l = m + 1
        else:
            h = m
    return l


def binary_search(nums: List[int], k: int) -> int:
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
    return -1


def partial_bs(nums: List[int], k: int) -> int:
    if len(nums) == 1 and nums[0] != k:
        return -1

    pivot = find_pivot(nums)
    
    left = binary_search(nums[:pivot], k)
    right = binary_search(nums[pivot:], k)

    if left != -1:
        return pivot + left
    elif right != -1:
        return pivot + right
    return -1


def single_binary_search(nums: List[int], k: int) -> int:
    n = len(nums)
    l, h = 0, n - 1

    while l <= h:
        m = l + (h - l) // 2

        if nums[m] == k:
            return m

        # If left half is sorted, check if the k lies in the left half
        if nums[m] >= nums[l]:
            if k >= nums[l] and k < nums[m]:
                h = m - 1
            else:
                l = m + 1
        else:
            if k <= nums[h] and k > nums[m]:
                l = m + 1
            else:
                h = m - 1
    return -1