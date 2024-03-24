#!/usr/bin/python3
"""
Module for calculating the fewest number of operations needed to
result in exactly n H characters in the file.
"""
import random



def min_operations(n):
    """
    Calculate the minimum number of operations needed to
    get n H characters in the file.

    :param n: int, the number of H characters to get in the file
    :return: int, the minimum number of operations needed to get n H characters
    """
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 1
        else:
            dp[i] = min(dp[i - 1], dp[i - 2] + 1)
    return dp[n]
