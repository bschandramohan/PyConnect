from functools import wraps


def metrics(fn):
    num_calls = 0
    name = fn.__name__

    @wraps(fn)
    def wrapper(*args, **kwargs):
        nonlocal num_calls
        num_calls += 1
        print(f"{name} called {num_calls} times")
        return fn(*args, **kwargs)
    return wrapper


@metrics
def add(a, b):
    return a + b


@metrics
def subtract(a, b):
    return a - b


print(add(2, 1))
print(add(12, 1))
print(subtract(12, 1))
