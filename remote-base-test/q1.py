import functools


def log_args_and_return(func):
    @functools.wraps(func)
    def wrapper(*args):
        # Log the input arguments
        print(f"LOG: {func.__name__}{args}")

        result = func(*args)

        return result

    return wrapper


# Example usage:
@log_args_and_return
def add(a, b):
    return a + b


@log_args_and_return
def subtract(a, b):
    return a - b


result1 = add(2, 3)
result2 = subtract(5, 2)
