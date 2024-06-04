#!/usr/bin/python3
"""
This module reads from stdin line by line and computes metrics.
"""

import sys
import signal

# Initialize variables
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
line_count = 0


def print_stats():
    """
    This function prints the statistics.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """
    This function handles keyboard interruption.
    """
    print_stats()
    sys.exit(0)


# Handle keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            size = int(parts[-1])
            status_code = int(parts[-2])
            total_size += size
            if status_code in status_codes:
                status_codes[status_code] += 1
        except:
            continue

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass

finally:
    print_stats()
