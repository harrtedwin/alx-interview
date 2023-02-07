#!/usr/bin/python3
"""
 Unlocked the boxes
"""


def canUnlockAll(boxes):
    """
        Look if the box is unlocked or not
        Return true if is unlocked or false
    """

    # Look to the unlocked boxes
    unlocked_box = [0]
    for i in unlocked_box:
        for j in boxes[i]:
            if j < len(boxes):
                if j not in unlocked_box:
                    unlocked_box.append(j)

    # Look the the length of the open box and all the boxes
    if len(boxes) == len(unlocked_box):
        return True
    else:
        return False
