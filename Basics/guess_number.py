#!/usr/bin/env python3
"""This is a guess the number game."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from random import randint


def main():
    """Entry point."""
    secret_number = randint(1, 20)
    print('I am thinking of a number between 1 and 20.')

    # Ask the player to guess 6 times.
    for guesses_taken in range(1, 7):
        guess = int(input('Take a guess > '))
        if guess < secret_number:
            print('Your guess is too low.')
        elif guess > secret_number:
            print('Your guess is too high.')
        else:
            print(f'Good job! You guessed my number in {guesses_taken} '
                  'guesses!')
            break
    else:
        print(f'Nope. The number I was thinking of was {secret_number}.')


if __name__ == '__main__':
    main()
