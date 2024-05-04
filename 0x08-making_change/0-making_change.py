#!/usr/bin/python3
"""
Module for making change problem
Provide functions to determine the minimum number
of coins needed to make change for a given amount
"""


def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to make change
    for a given amount

    Parameters:
    coins (list): a list of the values of the coins
    total (int): the total amount for which to make change

    Returns:
    int: The fewest  number of coins needed to make change for total
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0
    remaining = total

    for coin in coins:
        if remaining <= 0:
            break

        num_coins += remaining // coin
        remaining = remaining % coin

    if remaining != 0:
        return -1

    return num_coins
