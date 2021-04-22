#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
    """

    keyStack = [0]

    for iterator in keyStack:
        for key in boxes[iterator]:
            if key < len(boxes):
                if key in keyStack:
                    pass
                else:
                    keyStack.append(key)

    if len(keyStack) == len(boxes):
        return True
    else:
        return False
