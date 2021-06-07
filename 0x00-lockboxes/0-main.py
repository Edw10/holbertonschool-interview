#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1,9,8], [], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[]]
print(canUnlockAll(boxes))
