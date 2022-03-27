#!/usr/bin/env python3
"""swordfish.py: "continue" statement example."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def main():
    """Starting point."""
    while True:
        name = input('Who are you? ')

        if name.lower() != 'joe':
            continue

        print('Hello, Joe. What is the password? (It is a fish.)')
        password = input()

        if password == 'swordfish':
            break

    print('Access granted.')


if __name__ == '__main__':
    main()
