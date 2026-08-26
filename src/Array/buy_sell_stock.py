"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

from src.res.Array.buy_sell_stock import input as ip, output as op
from typing import List
from validator import are_two_arrays_same


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p

    # result = buy_sell_stock(arr)
    result = two_pointer_buy_sell(arr)
    print(result)

    if not result == op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', result)


def buy_sell_stock(prices: List[int]) -> int:
    """
    Note the minimum price to buy so far and max profit so far
    Args:
        List of prices
    Returns:
        Maximum profit
    """
    n = len(prices)
    min_price = prices[0]
    max_profit = 0
    i = 1

    while i < n:
        max_profit = max(max_profit, prices[i] - min_price)
        i += 1
        min_price = min(prices[i-1], min_price)

    return max_profit


def two_pointer_buy_sell(prices: List[int]) -> int:
    """
    Track the buy and sell using 2 pointers
    Args:
        List of prices
    Returns:
        Maximum profit
    """
    n = len(prices)
    buy = 0
    sell = 1
    max_profit = 0

    while sell < n:
        if prices[sell] > prices[buy]:
            max_profit = max(max_profit, prices[sell] - prices[buy])
        else:
            buy = sell
        sell += 1

    return max_profit
    
