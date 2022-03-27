#!/usr/bin/env python3
"""This program says hello and asks for my name."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def main():
    """Entry point."""
    my_name = input('What is your name? ')  # ask for their name.
    print(f'It is good to meet you, {my_name.title()}.')
    print(f'The length of your name is: {len(my_name)}')
    my_age = int(input('What is your age? '))  # ask for their age.
    print(f'You will be {my_age + 1} in a year.')


if __name__ == '__main__':
    main()
