"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Examples -

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

from src.res.Array.longest_common_prefix import input as ip, output as op
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
        results.append(longest_common_prefix_btw_words(n))
    print(results)

    if not are_two_arrays_same(results, op.o_p):
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def longest_common_prefix_sorted(strs: List[str]) -> str:
    """
    This function returns the longest common string
    in all the array elements sorting the words
    to compare first and last only
    Args:
        strs: List of strings
    Returns:
        str: Longest common prefix
    """
    sorted_strs = sorted(strs)
    first, last = sorted_strs[0], sorted_strs[-1]

    i = 0
    lcp = ""
    min_len = min(len(first), len(last))
    while i < min_len:
        if first[i] != last[i]:
            return lcp
        lcp += first[i]
        i += 1

    return lcp


def longest_common_prefix_btw_words(strs: List[str]) -> str:
    """
    This function return lcp by comparing all words
    by removing a letter each time lcp does not match
    :param strs: List of strings
    :return: Longest common prefix
    """
    pref = strs[0]
    pref_len = len(pref)

    for word in strs[1:]:
        while pref != word[0:pref_len]:
            pref_len -= 1
            if pref_len == 0:
                return ""
            pref = pref[0:pref_len]
    return pref
