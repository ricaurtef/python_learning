#!/usr/bin/env python3
"""print_random.py: modules example."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'

from random import randint


def main():
    """Starting point."""
    print('Random numbers:', *(randint(1, 10) for _ in range(5)))


if __name__ == '__main__':
    main()
