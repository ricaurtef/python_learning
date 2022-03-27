#!/usr/bin/env python3
"""'if' statement exercise."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def main():
    """Entry point."""
    name = 'carol'
    age = 3000

    if name == 'alice':
        print('Hi, Alice.')
    elif age < 12:
        print('You are not Aice, kiddo.')
    elif age > 2000:
        print('Unlike you, Alice is not an undead, immortal vampire.')
    elif age > 100:
        print('You are not Alice, grannie.')


if __name__ == '__main__':
    main()
