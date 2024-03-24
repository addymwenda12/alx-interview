#!/usr/bin/python3
"""
Module for calculating the fewest number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters in the file.
    
    Args:
        n (int): The desired number of H characters.
        
    Returns:
        int: The fewest number of operations needed. If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1
    
    return operations
