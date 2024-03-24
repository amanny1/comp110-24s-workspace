"""Summing the elements of a list using different loops."""


__author__ = "730668694"


def w_sum(vals: list[float]) -> float:
    """Calculate the sum of a list of floats using a while loop."""
    total = 0.0
    index = 0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Calculate the sum of a list of floats using a for loop with direct iteration."""
    total = 0.0
    for val in vals:
        total += val
    return total


def f_range_sum(vals: list[float]) -> float:
    """Calculate the sum of a list of floats using a for loop with range."""
    total = 0.0
    for index in range(len(vals)):
        total += vals[index]
    return total