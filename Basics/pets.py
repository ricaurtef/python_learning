#! /usr/bin/env python3
"""Passing Arguments to Functions."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f'I have a {animal_type}.\n'
          f'My {animal_type}\'s name is {pet_name.title()}.')


def main():
    """Starting point of the program."""
    pets = [('harry', 'hamster'), ('willie',)]
    for pet in pets:
        describe_pet(*pet)


if __name__ == '__main__':
    main()
