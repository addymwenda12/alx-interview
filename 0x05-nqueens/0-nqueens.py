#!/usr/bin/python3
"""
This module contains the class for N-Queen chess
"""
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place the queen

    Parameters:
    board (list): The chess borad represented as a 2D
    row (int): The row index of the position
    col (int): The column index of the position
    """
    for i in range(row):
        if board[i] == col:
            return False

    # Check if there is a queen in the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row):
    """
    Solves the N-Queens problem using recursion and backtracking

    Parameters:
    board (list): The chess board represented as a 2D list.
    row (int): The current row index

    Returns:
    None
    """
    if row == N:
        print(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1)
            board[row] = -1


def nqueens(N):
    """
    Entry point of the program that initializes and calls the solver function

    Parameters:
    N (int): Size of the chess board

    Returns:
    None
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve_nqueens(board, 0)

if __name__ == "__main__":
    """
    Main block to run the program when it's executed directly
    from the command line
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
