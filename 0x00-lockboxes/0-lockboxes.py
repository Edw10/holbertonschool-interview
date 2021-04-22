#!/usr/bin/python3
""" can be unlocked? """


def canUnlockAll(boxes):
    """ function to determine if the boxes can be open  """
    o_b = []
    p = 0
    for y in boxes:
        for i in y:
            if i not in o_b:
                o_b.append(i)
    for e in range(1, len(boxes)):
        if e in o_b:
            if len(boxes) - 1 == e:
                return True
        else:
            return False
    return True
