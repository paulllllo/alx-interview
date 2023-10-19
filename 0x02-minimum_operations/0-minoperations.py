#!/usr/bin/python3
"""
Defines function that Calculates the minimum number of operations
"""


def minOperations(n):
    """Calculates the minimum no of operations"""
    current = 1
    copy = 0
    opr = 0

    if n < current:
        return 0

    def copyAll():
        """Copies all chars in file"""
        nonlocal opr, copy, current
        opr = opr + 1
        copy = current
        return

    def paste():
        """pastes copied chars"""
        nonlocal opr, copy, current
        opr = opr + 1
        current = current + copy
        return

    while current <= n:
        if current == n:
            return opr
        if (n - current) == copy:
            paste()
            continue
        if ((n % (current + copy) == 0) and (current + copy != 1)):
            paste()
            continue
        if copy >= current:
            paste()
            continue
        copyAll()
        paste()
    return 0
