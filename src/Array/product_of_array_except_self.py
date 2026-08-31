"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
from src.res.Array.product_of_array_except_self import input as ip, output as op
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
        results.append(split_array(arr))
    print(results)

    if not are_two_arrays_same(results, op.o_p):
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def brute_force(nums: List[int]) -> List[int]:
    n = len(nums)

    res = []
    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= nums[j]
        res.append(prod)

    return res


def split_array(nums: List[int]) -> List[int]:
    """
    Calculate the products of the elements to the left
    prod_left[0] = 1 (always as there is no element on the left)
    prod_left[1] = nums[0] * prod_left[0]
    prod_left[2] = nums[1] * prod_left[1], and so on

    Calculate the products of the elements to the right (start from extreme right for this)
    prod_right[n-1] = 1
    prod_right[n-2] = prod_right[n-1] * nums[n-1] and so on
    """
    n = len(nums)
    res = [1] * n

    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]

    return res
