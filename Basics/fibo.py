"""Fibonacci numbers module."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


# Write Fibonacci series up to n.
def fib(n):
    a, b = 0, 1

    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# Write Fibonacci series up to n.
def fib2(n):
    result = []
    a, b = 0, 1

    while a < n:
        result.append(a)
        a, b = b, a+b

    return result
