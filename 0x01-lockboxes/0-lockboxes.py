#!/usr/bin/python3
"""
It contains a function called canUnlockAll that determines
whether all the boxes in a given list can be unlocked.

The canUnlockAll function takes a list of boxes as
input and returns True if all the boxes can be unlocked,
and False otherwise.
"""


def canUnlockAll(boxes):
    """
    Check if all boxes in the given list can be unlocked.

    Args:
        boxes (list): A list of lists representing the
        lockboxes and their corresponding keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    # Create a set to keep track of the boxes that have been visited
    visited = set()
    # Add the first box to the visited set
    visited.add(0)
    # Create a stack to store the boxes that need to be visited
    stack = [0]
    
    # Iterate through the stack until it is empty
    while stack:
        # Pop the top box from the stack
        current_box = stack.pop()
        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            # If the key opens a new box and the box has
            # not been visited yet, add it to the stack
            if key < len(boxes) and key not in visited:
                # Add the box to the visited set
                visited.add(key)
                # Add the box to the stack to be visited later
                stack.append(key)
    
    # If all boxes have been visited, return True
    if len(visited) == len(boxes):
        return True
    # Otherwise, return False
    else:
        return False
