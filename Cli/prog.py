#!/usr/bin/env python3
"""Argparse examples."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from argparse import ArgumentParser


def args():
    """Handle command-line arguments and options."""
    parser = ArgumentParser()

    # Example 01: positional arguments.
    # parser.add_argument('echo', help='echo the string you use here')

    # Example 02: positional arguments.
    # parser.add_argument('square', type=int,
    #                     help='display a square of a given number')

    # Example 03: optional arguments.
    # parser.add_argument('-v', '--verbose', action='store_true',
    #                     help='increase output verbosity')

    # Example 04: combining positional and optional arguments.
    # parser.add_argument('square', type=int,
    #                     help='display a square of a given number')
    # parser.add_argument('-v', '--verbose', action='store_true',
    #                     help='increase output verbosity')

    # Example 05: combining positional and optional arguments.
    parser.add_argument('square', type=int,
                        help='display a square of a given number')
    parser.add_argument('-v', '--verbosity', action='count', default=0,
                        help='increase output verbosity')
    return parser.parse_args()


def main():
    """Entry point."""
    argv = args()

    # Example 01.
    # print(argv.echo)

    # Example 02.
    # print(pow(argv.square, 2))

    # Example 03.
    # if argv.verbose:
    #     print('Verbosity turned on.')

    # Example 04.
    # answer = pow(argv.square, 2)

    # if argv.verbose:
    #     print(f'the square of {argv.square} equals {answer}')
    # else:
    #     print(answer)

    # Example 05.
    answer = pow(argv.square, 2)

    if argv.verbosity >= 2:
        print(f'the square of {argv.square} equals {answer}')
    elif argv.verbosity == 1:
        print(f'{argv.square}^2 == {answer}')
    else:
        print(answer)


if __name__ == '__main__':
    main()
