#!/usr/bin/python3
"""ALX SE log parsing"""

import sys
from collections import defaultdict


def process_line(line):
    """split every line to capture needed output"""
    parts = line.strip().split()
    if len(parts) != 9:
        return None, None

    status_code = parts[-2]

    try:
        file_size = int(parts[-1])
        status_code = int(status_code)
    except ValueError:
        return None, None

    return file_size, status_code


def print_metrics(total_size, status_codes_count):
    """print the metric to stdout"""
    print(f"File size: {total_size}")

    for status_code in sorted(status_codes_count.keys()):
        print(f"{status_code}: {status_codes_count[status_code]}")


def main():
    """main entry"""
    total_size = 0
    status_codes_count = defaultdict(int)
    line_number = 0

    try:
        for line in sys.stdin:
            line_number += 1

            file_size, status_code = process_line(line)
            if file_size is None or status_code is None:
                continue

            total_size += file_size
            status_codes_count[status_code] += 1

            if line_number % 10 == 0:
                print_metrics(total_size, status_codes_count)
    finally:
        print_metrics(total_size, status_codes_count)


main()
