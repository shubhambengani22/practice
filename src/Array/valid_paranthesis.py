"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false
"""
from src.res.Array.valid_paranthesis import input as ip, output as op
from validator import are_two_arrays_same


def solve():
    """
    The solution of the program
    :return: None
    """
    input = ip.i_p
    results = []

    for inp in input:
        results.append(stack_approach(inp))
    print(results)

    if not are_two_arrays_same(results, op.o_p):
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def stack_approach(s: str) -> bool:
    source = {')': '(', '}': '{', ']': '['}
    stack = []

    for bracket in s:
        if bracket in source:
            if not stack or stack[-1] != source[bracket]:
                return False
            stack.pop()
        else:
            stack.append(bracket)
    return len(stack) == 0
