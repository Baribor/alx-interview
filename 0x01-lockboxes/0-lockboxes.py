#!/usr/bin/python3
"""
Developed a function to check if all boxes can be
opened given a list of boxes
"""

def canUnlockAll(boxes):
    """Checks if all boxes can be opened

    Args:
            boxes (List[List]): a list of list of integers
    """
    n = len(boxes)
    allBoxes = [False if i > 0 else True for i in range(n)]
    for box in boxes:
        if len(box) == 0:
            break
        for key in box:
            if key <= n - 1:
                allBoxes[key] = True
    return all(allBoxes)
