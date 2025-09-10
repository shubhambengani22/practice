"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Examples:

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

from src.res.Array.two_sum import input as ip, output as op

difficulty = "Easy"


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(sorted(two_sum_single_pass(n[0], n[1])))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def two_sum_hashmap(nums, target):
    """
    This function finds 2 numbers whose sum equals target.
    This approach is done in 2 pass
    Args:
        nums: The list of elements
        target: The target sum
    Returns:
        List: Indices of the two numbers adding to target
    """
    diff_map = {}

    for i in range(len(nums)):
        diff_map[nums[i]] = i

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff_map.get(diff, None):
            return [diff_map[diff], i]

    return []


def two_sum_single_pass(nums, target):
    """
        This function finds 2 numbers whose sum equals target.
        This approach is done in a single pass
        Args:
            nums: The list of elements
            target: The target sum
        Returns:
            List: Indices of the two numbers adding to target
        """
    nums_to_idx = {}
    for i, n in enumerate(nums):
        diff = target - n
        # Populate values in dict, for the first time, lets say,
        # target = 9, nums[0] = 2, and 7 is present in nums,
        # It will populate 2 in the dict and later find it when it
        # encounters 7.
        if diff in nums_to_idx:
            return [nums_to_idx[diff], i]
        nums_to_idx[n] = i

    return []
