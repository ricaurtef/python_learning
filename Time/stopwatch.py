#!/usr/bin/env python3
"""A simple stopwatch program."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import time


def main():
    """Entry point."""
    # Display the program's instructions.
    print('Press ENTER to begin. Afterward, press ENTER to "click" the '
          'stopwatch.\n(Press Ctrl-C to quit)')
    input()  # Enter to begin.
    print('Started.')
    start_time = time.time()  # The first lap's start time.
    last_time = start_time
    lap_num = 1

    try:
        while True:
            input()
            lap_time = time.time() - last_time
            total_time = time.time() - start_time
            print(f'Lap {lap_num}: {total_time:.2f} ({lap_time:.2f})', end='')
            lap_num += 1
            last_time = time.time()  # Reset the last lat time.
    except KeyboardInterrupt:
        print('\nDone.')


if __name__ == '__main__':
    main()
