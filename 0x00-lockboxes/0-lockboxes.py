#!/usr/bin/python3
""" can be unlocked? """


def canUnlockAll(boxes):
    """ function to determine if the boxes can be open  """
    o_b = []
    for y in o_b:
        if y <= len(boxes):
            for i in boxes[y]:
                if i not in o_b:
                    o_b.append(i)
    if all(x in o_b for x in range(1, len(boxes))):
        if len(boxes) - 1 == len(o_b):
            return True
        else:
            return False
    return True
