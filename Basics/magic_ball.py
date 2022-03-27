#!/usr/bin/env python3
"""Introduction to functions."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from random import choice


def get_answer():
    """The power of the magic 8 ball."""
    answer = (
        'It is certain.',
        'It is decidedly so.',
        'Yes',
        'Reply hazy try again.',
        'Ask again later.',
        'Concentrate and ask again.',
        'My reply is no.',
        'Outlook not so good.',
        'Very doubtful.',
    )
    return choice(answer)


if __name__ == '__main__':
    print(get_answer())
