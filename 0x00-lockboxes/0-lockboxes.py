#!/usr/bin/python3
""" can be unlocked? """


def canUnlockAll(boxes):
    """ function to determine if the boxes can be open  """
    o_b = [0]
    for y in o_b:
        if y <= len(boxes):
            for i in boxes[y]:
                if i not in o_b:
                    o_b.append(i)
    if any(x not in range(len(boxes)) for x in o_b):
        return False
    if len(o_b) == len(boxes):
        return True
    return False
