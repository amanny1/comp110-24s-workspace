"""Splitting a dictionary into two lists."""

__author__ = "730669694"


test: dict[str, int] = {"Hello": 1, "World": 2}


def get_keys(dict1: dict[str, int]) -> list[str]:
    """Returns the keys of the dictionary in a list."""
    list1: list[str] = list()
    for index in dict1:
        list1.append(index)
    print(list1)
    return list1


get_keys(test)


def get_values(dict2: dict[str, int]) -> list[int]:
    """Returns the values of the dictionary in a list."""
    list2: list[int] = list()
    for index in dict2:
        list2.append(dict2[index])
    print(list2)
    return list2


get_values(test)