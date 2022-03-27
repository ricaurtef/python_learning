#! /usr/bin/env python3
"""Challenge: Track Your Investments.

Track the growing amount of an investment over time.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def invest(amount, rate, years):
    """Display year on year growth of an initial investment."""
    rate = 1 + (rate / 100)

    for year in range(1, years+1):
        amount *= rate
        print(f'year {year}: ${amount:,.2f}')


def main():
    """Starting point of the program."""
    principal_amount = float(input('Enter initial amount: '))
    annual_rate = int(input('Enter annual rate [%]: '))
    years = int(input('Enter number of years: '))

    # Display the calculations for the values entered by the user.
    invest(principal_amount, annual_rate, years)


if __name__ == '__main__':
    main()

