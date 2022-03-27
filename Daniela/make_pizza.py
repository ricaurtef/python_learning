#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = {
    'author': 'Daniela Itriago <danielaitriago@gmail.com>',
    'collaborator': 'Ruben Ricaurte <ricaurtef@gmail.com>',
}


# Global definitions.
pizzas = {
    'common': ('pepperoni', 'bacon'),
    'veggie': ('veggie 1', 'veggie 2'),
}


def get_options(banner, prompt, elements):
    """TODO: Function docstring."""
    print(banner)
    for i, element in enumerate(elements):
        print(f'{i+1}. {element.title()}')
    option = int(input(f'{prompt} > '))

    return option


def get_pizza_type(pizza_type):
    """Return the type of pizza selected by the customer."""

    return tuple(pizzas)[pizza_type - 1]


def get_topping(pizza_type, topping):
    """Return a topping for a given type of pizza."""

    return pizzas[pizza_type][topping - 1]


def main():
    """Starting point of the program."""
    # Display the menu and get a type of pizza.
    pizza_banner = "Welcome to Daniela's Pizza!\n\nThese are our specialties:"
    pizza_prompt = 'What would you like to order?'
    pizza_option = get_options(pizza_banner, pizza_prompt, pizzas)
    pizza = get_pizza_type(pizza_option)

    # Get the topping.
    topping_banner = f'These are the toppings for a "{pizza.title()}" pizza:'
    topping_prompt = 'Select a topping'
    topping_option = get_options(topping_banner, topping_prompt, pizzas[pizza])
    topping = get_topping(pizza, topping_option)

    # Order summary.
    print(f'You ordered a {pizza} pizza with {topping}. Coming right up!')


if __name__ == '__main__':
    main()
