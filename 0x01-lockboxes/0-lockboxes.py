#!/usr/bin/python3
"""
It contains a function called canUnlockAll that determines
whether all the boxes in a given list can be unlocked.

The canUnlockAll function takes a list of boxes as
input and returns True if all the boxes can be unlocked, and False otherwise.

The algorithm used in the canUnlockAll function is as follows:
1. Create a set called visited to keep track of the boxes that have been visited.
2. Add the first box (index 0) to the visited set.
3. Create a stack to store the boxes that need to be visited, and initialize it with the first box.
4. Iterate through the stack until it is empty:
    - Pop the top box from the stack.
    - Iterate through the keys in the current box.
    - If the key opens a new box (index within the range of the boxes list) and the box has not been visited yet, add the box to the visited set and push it onto the stack.
5. After the iteration, if the number of visited boxes is equal to the total number of boxes, return True. Otherwise, return False.
"""


def canUnlockAll(boxes):
    """
    Check if all boxes in the given list can be unlocked.

    Args:
        boxes (list): A list of lists representing the lockboxes and their corresponding keys.

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
            # If the key opens a new box and the box has not been visited yet
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