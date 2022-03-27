"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from functools import wraps
from time import perf_counter, sleep


# Measure the time a function take to execute.
def timer(func):
    """Print the runtime of the decorated function."""
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print(f'Finished {func.__name__!r} in {run_time:.4f} secs')

        return value

    return wrapper_timer


# Print the arguments a function is called with as well as its return value.
def debug(func):
    """Print the function signature and return value."""
    @wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')
        value = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {value!r}')

        return value

    return wrapper_debug


# It will sleep one second before it calls the decorated function.
def slow_down(func):
    """Sleep 1 second before calling the function."""
    def wrapper_slow_down(*args, **kwargs):
        sleep(1)

        return func(*args, **kwargs)

    return wrapper_slow_down
