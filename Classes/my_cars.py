#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from car import Car, ElectricCar as EC


def main():
    """Starting point of the program."""
    cars = {
        'beetle': ('volkswagen', 'beetle', 2019),
        'tesla': ('tesla', 'roadster', 2019),
    }

    for model, model_info in cars.items():
        my_car = Car(*model_info)
        if model == 'tesla':
            my_car = EC(*model_info)
        print(my_car)


if __name__ == '__main__':
    main()
