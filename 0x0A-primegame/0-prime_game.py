#!/usr/bin/python3
"""Prime Game"""


def prime_nums_in_range(start, end):
    """Finds and returns all the prime numbers in a range"""
    prime_numbers = []

    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)

    return prime_numbers


def isWinner(x, nums):
    """Returns the name of the winner that won the most rounds"""
    if not x or not nums:
        return None

    maria_score, ben_score = 0, 0
    for rounds in range(x):
        result = prime_nums_in_range(1, nums[rounds])
        if len(result) % 2:
            maria_score += 1
        else:
            ben_score += 1
    if maria_score > ben_score:
        return 'Maria'
    elif ben_score > maria_score:
        return 'Ben'
    else:
        return None
