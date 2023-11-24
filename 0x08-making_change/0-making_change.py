#!/usr/bin/python3
"""A function that determines the fewest number of coins needed to give a total"""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total"""
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    count = 0
    remaining_total = total

    for coin in sorted_coins:
        while remaining_total >= coin:
            remaining_total -= coin
            count += 1

        if remaining_total == 0:
            return count

    return -1
