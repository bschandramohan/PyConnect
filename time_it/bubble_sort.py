# Demonstrate decorator functions (@function) and a sample algorithm
import time


def time_it_without_args(to_time_function):
    current_time_in_ns = time.time_ns()
    result = to_time_function()
    print(f"Time Taken for {to_time_function.__name__} is {time.time_ns() - current_time_in_ns}")
    return result


# This doesn't work
# def time_it_with_args(to_time_function, *args, **kwargs):
#     current_time_in_ns = time.time_ns()
#     result = to_time_function(*args, **kwargs)
#     print(f"Time Taken for {to_time_function.__name__} is {time.time_ns() - current_time_in_ns}")
#     return result


def time_it(to_time_function):
    # TODO: Figure out why this sub method is required for arguments method
    def timed(*args, **kwargs):
        current_time_in_ns = time.time_ns()
        result = to_time_function(*args, **kwargs)
        print(f"Time Taken for {to_time_function.__name__} is {time.time_ns() - current_time_in_ns}")
        return result

    return timed


@time_it_without_args
def long_operation():
    total = 0
    for i in range(0, 1000000):
        total += i
    return total


@time_it
def bubble_sort(numbers):
    list_len = len(numbers)
    for j in range(list_len - 1):
        for i in range(list_len - j - 1):
            if numbers[i] > numbers[i + 1]:
                # Swap
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
    return numbers


given_numbers = [11, 22, 4, 13, 2]
print("Given numbers=", given_numbers)
sorted_numbers = bubble_sort(given_numbers)
print("Sorted numbers=", sorted_numbers)

