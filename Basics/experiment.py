#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from random import choice


def coin_flip():
    """Randomly return 'heads' or 'tails'."""

    return choice(('heads', 'tails'))


def main():
    """Starting point of the program."""
    heads_tally = tails_tally = 0

    for _ in range(10_000):
        if coin_flip() == 'heads':
            heads_tally += 1
        else:
            tails_tally += 1

    # Display the ratio of heads and tails.
    ratio = heads_tally / tails_tally
    print(f'The ratio of heads to tails is {ratio:.2f}.')


if __name__ == '__main__':
    main()
