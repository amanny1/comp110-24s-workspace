"""Mutating Functions."""


__author__ = "730668694"


def manual_append(numbers: list[int], value: int) -> None:
    """Appends an integer value to the end of a list of integers."""
    numbers.append(value)


a = [1, 2, 3]
manual_append(a, 2)
print(a)


def double(numbers: list[int]) -> None:
    """Doubles each element in a list of integers."""
    i = 0
    while i < len(numbers):
        numbers[i] *= 2
        i += 1


b = [1, 2, 3]
double(b)
print(b)