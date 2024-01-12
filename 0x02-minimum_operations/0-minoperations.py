#!/usr/bin/python3
"""ALX SE"""


def minOperations(n: int) -> int:
    """Return the minimum number of operations to complete a task"""
    if n <= 1:
        return 0

    divisor = 2
    operations = 0

    while (n > 1):
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1
    return operations
