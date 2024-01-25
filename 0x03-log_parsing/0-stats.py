#!/usr/bin/python3
"""ALX SE log parser solution"""
import sys
import re
import signal

if __name__ == "__main__":
    total_file_size = 0
    status_code_cnt = {}
    line_count = 0

    pattern = r"(\S+) - \[(.+)\] \"GET /projects/260 HTTP/1.1\" (\d+) (\d+)"

    def print_metrics():
        """print the statistics of the metrix on status codes"""
        global total_file_size, status_code_cnt
        print("File size: {}".format(total_file_size))
        for status in sorted(status_code_cnt):
            print("{}: {}".format(status, status_code_cnt[status]))

    try:
        for line in sys.stdin:
            line_count += 1
            match = re.match(pattern, line)
            if match:
                ip, date, status, size = match.groups()
                size = int(size)
                total_file_size += size
                status_code_cnt[status] = status_code_cnt.get(
                    status, 0) + 1
                if line_count % 10 == 0:
                    print_metrics()
                    line_count += 1
    except KeyboardInterrupt:
        """if keyboard interrupt: print stats and exit"""
        print_metrics()
        sys.exit()
