#! /usr/bin/env python3
"""Error Handling: ZeroDivisionError."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def get_operands():
    """Prompt for the values with which to operate."""
    operands = []

    while (i := len(operands)) != 2:
        operand = input(f'Enter number [{i+1}]: ').lower()
        if operand == 'q':
            exit()
        try:
            operands.append(int(operand))
        except ValueError:
            print('Please, enter a number.')
            continue

    return operands


def division(dividend, divider):
    """Perform a division on the given values."""
    try:
        answer = dividend / divider
    except ZeroDivisionError as err:
        result = f'Error: {err}'
    else:
        result = f'{answer:,.2f}'

    return result


def main():
    """Starting point of the program."""
    print("Give me two numbers, and I'll divide them. (Enter 'q' to quit)\n")
    num1, num2 = get_operands()
    print(division(num1, num2))


if __name__ == '__main__':
    main()
