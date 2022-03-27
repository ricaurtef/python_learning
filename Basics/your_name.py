#!/usr/bin/env python3
"""An annoying while loop."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def main():
    """Entry point."""
    while True:
        name = input('Please type your name > ').lower()
        if name == 'your name':
            break
    print('Thank you!')


if __name__ == '__main__':
    main()
