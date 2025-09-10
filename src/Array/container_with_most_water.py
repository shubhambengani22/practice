"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Examples -

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""

from src.res.Array.container_with_most_water import input as ip, output as op
from typing import List
from validator import are_two_arrays_same


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(max_area(n))
    print(results)

    if not are_two_arrays_same(results, op.o_p):
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def max_area(height: List[int]) -> int:
    """
    This function finds maximum area of water that.
    can be held inside the container
    Approach: 2-pointer
    Args:
        height: The height of the lines forming the container
    Returns:
        int: maximum area
    """
    n = len(height)
    l, r = 0, n-1

    maxarea = 0

    while l <= r:
        maxarea = max(maxarea, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return maxarea
