# 0x01. Lockboxes

## Concepts to Understand
- Lists and List Manipulation: 

Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically. [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/introduction.html#lists)
- Graph Theory Basics: 

Although not explicitly required, knowledge of graph theory (especially concepts related to traversal algorithms like Depth-First Search or Breadth-First Search) can be very helpful in solving this problem, as the boxes and keys can be thought of as nodes and edges in a graph. [Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs)

- Algorithmic Complexity: 

Understanding the time and space complexity of your solution is important, as it can help in writing more efficient algorithms. [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/)
- Recursion: 

Some solutions might require a recursive approach to traverse through the boxes and keys. [Recursion in Python (Real Python)](https://realpython.com/python-thinking-recursively/)
- Queue and Stack:

 Knowing how to use queues and stacks is crucial if implementing a breadth-first search (BFS) or depth-first search (DFS) algorithm to traverse through the keys and boxes. [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/stack-queue-python-using-module-queue/)
- Set Operations: Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process. [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#sets)

## Description

This project involves solving a problem related to graph traversal and list manipulation in Python. The problem is as follows:

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from 0 to `n - 1` and each box may contain keys to the other boxes.

The task is to write a method that determines if all the boxes can be opened.

## Function Prototype

```python
def canUnlockAll(boxes: List[List[int]]) -> bool:
```

## Parameters
- `boxes`: A list of lists representing the boxes and their corresponding keys needed to open them.

- A key with the same number as a box opens that box

- You assume all keys will be positive integers

- There can be keys that do not have boxes

- The first `boxes[0]` unlocked

## Return
- Return `True` if all boxes can be opened, else return `False`