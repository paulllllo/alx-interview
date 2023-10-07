#!/usr/bin/python3
"""
A module that solves a logical problem
"""


def canUnlockAll(boxes):
    """ Function to calculate if a box can be opened or not """

    opened = [0]
    keyholder = []

    def is_open(box_i):
        return box_i in opened

    def add_keys(box):
        changed = False
        for key in box:
            if key not in keyholder:
                keyholder.append(key)
                changed = True
        return changed

    def add_box(index):
        opened.append(index)

    def find_key(index):
        return index in keyholder

    for index in range(len(boxes)):
        if is_open(index):
            add_keys(boxes[index])
        else:
            if find_key(index):
                add_box(index)
                add_keys(boxes[index])
            else:
                recurse = True
                while recurse:
                    recurse = False
                    for key in keyholder:
                        if key < len(boxes):
                            if not is_open(key):
                                add_box(key)
                                recurse = add_keys(boxes[key])
                                if find_key(index):
                                    add_box(index)
                                    add_keys(boxes[index])
                                    recurse = False
                                    break
                if not find_key(index):
                    return False

    return True
