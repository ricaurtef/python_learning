#! /usr/bin/env python3
"""Classes: Creating a Dog Class."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name.title()
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a commnad."""
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f'{self.name} rolled over.')


def main():
    """Starting point of the program."""
    # my_dog = Dog
    # Dog.__init__(my_dog, 'willie', 6)
    dogs = {
        'My dog': ('willie', 6),
        'Your dog': ('lucy', 3),
    }

    for owner, dog_info in dogs.items():
        dog = Dog(*dog_info)
        print(f"{owner}'s name is {dog.name}.\n"
              f"{owner} is {dog.age} years old.")
        dog.sit()
        dog.roll_over()
        print()


if __name__ == '__main__':
    main()
