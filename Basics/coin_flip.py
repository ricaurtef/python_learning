#! /usr/bin/env python3
"""Functions: Exercise.

Write a program to find out how often a streak of six heads or a streak
of six tails comes up in a randomly generated list of heads and tails.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from random import choice


def get_streaks(list_choices):
    """
    Returns the number of streaks 6 tails or heads that comes up in a
    given list.
    """
    streaks = 0

    for i in range(len(list_choices)):
        chunk = list_choices[i:i+6]
        if len(chunk) == 6 and len(set(chunk)) == 1:
            streaks += 1

    return streaks


def main():
    """Script entry point."""
    num_streaks = 0

    for _ in range(10000):
        # Creates list of randomly 'heads' and 'tails' values.
        choices = [choice(['H', 'T']) for _ in range(100)]
        num_streaks += get_streaks(choices)

    # Displaoy de outcome.
    print(f'Chance of streak: {num_streaks / 100:.2f}%')


if __name__ == '__main__':
    main()
