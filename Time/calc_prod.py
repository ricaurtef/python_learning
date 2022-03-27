#!/usr/bin/env python3
"""Profiling: Time module."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import time


def calc_prod(product=1, limit=100_000):
    """Calculate the product of the first 100,000 numbers."""
    for i in range(1, limit):
        product *= i

    return product


def main():
    """Entry point."""
    start_time = time.time()
    prod = str(calc_prod())
    end_time = time.time()
    print(f'The result is {len(prod)} digits long.')
    print(f'Took {end_time - start_time} secs to calculate.')


if __name__ == '__main__':
    main()
