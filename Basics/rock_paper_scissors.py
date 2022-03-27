#!/usr/bin/env python3
"""This is a simple rock, paper, scissors game."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from random import choice
import sys


def main():
    """Entry point."""
    print('Rock, paper, scissors')

    # These variables keep track of the number of wins, losses, and ties.
    wins, losses, ties = 0, 0, 0

    # The main game loop.
    while True:
        print(f'{wins} Wins, {losses} Losses, {ties} Ties')
        while True:  # The player input loop.
            player_move = input('Enter move [(r)ock (p)aper (s)cissors or '
                                '(q)uit] > ')[0].lower()
            if player_move == 'q':
                sys.exit()  # Quit the program.
            elif player_move in 'rps':
                break  # Break out of the player input loop.
            print('Wrong! Please enter r, p, s, or q.')

        # Display what the player chose.
        if player_move == 'r':
            print('Rock versus...')
        elif player_move == 'p':
            print('Paper versus...')
        else:
            print('Scissors versus...')

        # Display what the computer chose:
        computer_move = choice('rps')
        if computer_move == 'r':
            print('Rock')
        elif computer_move == 'p':
            print('Paper')
        else:
            print('Scissors')

        # Display and record the win/loss/tie:
        if player_move == computer_move:
            print('It is a tie.')
            ties += 1
        elif ((player_move == 'r' and computer_move == 's')
              or (player_move == 'p' and computer_move == 'r')
              or (player_move == 's' and computer_move == 'p')):
            print('You win!')
            wins += 1
        else:
            print('You lose!')
            losses += 1


if __name__ == '__main__':
    main()
