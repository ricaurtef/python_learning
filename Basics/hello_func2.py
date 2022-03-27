#!/usr/bin/env python3
"""Introduction to functions in python."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def hello(first_name):
    """Displays a greeting for a person."""
    print(f'Hello, {first_name.title()}.')


if __name__ == '__main__':
    for name in 'alice', 'bob':
        hello(name)
