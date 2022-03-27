#! /usr/bin/env python3
"""Modifying a list in a function."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from collections import deque
from time import sleep


def print_models(unprinted, completed, pause=3):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    unprinted_designs = deque(unprinted)

    while unprinted_designs:
        current_design = unprinted_designs.popleft()
        print(f'Printing model: {current_design}')
        completed.append(current_design)
        sleep(pause)


def show_completed_models(completed):
    """Show all the models that were printed."""
    print('\nThe following models have been printed:')
    for model in completed:
        print(model)


def main():
    """Starting point of the program."""
    unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
    completed_models = []

    print_models(unprinted_designs, completed_models)
    show_completed_models(completed_models)


if __name__ == '__main__':
    main()
