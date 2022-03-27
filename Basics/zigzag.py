#!/usr/bin/env python3
"""Exception handling example."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import sys
import time


def main():
    """Entry point."""
    indent = 0  # How many spaces to indent.
    indent_increasing = True  # Whether the indentation is increasing or not.
    try:
        while True:
            print(' ' * indent, end='')
            print('*' * 8)
            time.sleep(0.1)  # Pause for 1/10 of a second.
            if indent_increasing:
                # Increase the number of spaces:
                indent += 1
                if indent == 20:
                    # Change direction.
                    indent_increasing = False
            else:
                # Decrease the number of spaces.
                indent -= 1
                if not indent:
                    # Change direction.
                    indent_increasing = True
    except KeyboardInterrupt:
        print('Pretty cool, right!')
        sys.exit()


if __name__ == '__main__':
    main()
