#!/usr/bin/python3
"""
Prime Game Module

This module contains functions to simulate a game where two players take turns
to remove a prime number and its multiples from a set of consecutive integers.
The player who cannot make a move loses the game.
"""


def generate_primes(n):
    """
    Generate a list of booleans representing prime numbers up to n.

    Args:
        n (int): The upper limit for generating prime numbers.

    Returns:
        list: A list of booleans where the index represents the number and
              the value at that index represents whether the number is prime.
    """
    primes = [False, False] + [True for _ in range(n-1)]
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    return primes


def play_round(n):
    """
    Simulate a round of the game with a maximum number n.

    Args:
        n (int): The maximum number for the round.

    Returns:
        str: The name of the player who wins the round.
    """
    primes = generate_primes(n)
    player = 0
    while True:
        if any(primes):
            prime = primes.index(True)
            for i in range(prime, n + 1, prime):
                primes[i] = False
            player = 1 - player
        else:
            return 'Maria' if player else 'Ben'


def isWinner(x, nums):
    """
    Simulate x rounds of the game and determine the overall winner.

    Args:
        x (int): The number of rounds.
        nums (list): A list of maximum numbers for each round.

    Returns:
        str: The name of the player who wins the most rounds,
        or None if there is a tie.
    """
    if x <= 0 or x > len(nums):
        return None

    scores = {'Maria': 0, 'Ben': 0}
    for n in nums:
        if n <= 0:
            scores['Ben'] += 1
        else:
            winner = play_round(n)
            scores[winner] += 1
    if scores['Maria'] > scores['Ben']:
        return 'Maria'
    elif scores['Maria'] < scores['Ben']:
        return 'Ben'
    else:
        return None
