#!/usr/bin/env python3
"""Using the loggin Module."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
logging.disable(logging.DEBUG)  # Comment out to enable logging.


# Logging start.
logging.debug('Start of program.')


def factorial(number):
    """Calculate the factorial of a given number."""
    total = 1
    logging.debug('Start of factorial(%d).', number)

    for i in range(1, number+1):
        total *= i
        logging.debug('i is %d, total is %d.', i, total)
    logging.debug('End of factorial(%d).', number)

    return total


def main():
    """Entry point."""
    print(factorial(5))
    logging.debug('End of program.')


if __name__ == '__main__':
    main()
