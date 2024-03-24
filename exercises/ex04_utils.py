"""Utility functions for list manipulations in EX04."""


__author__ = "730669694"


def all(nums: list[int], target: int) -> bool:
    """Check if all elements in the list are equal to the target integer."""
    for num in nums:
        if num != target:
            return False
    return True if nums else False


def max(nums: list[int]) -> int:
    """Return the largest integer in the list, or raise ValueError if the list is empty."""
    if len(nums) == 0:
        raise ValueError("max() arg is an empty List")
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Return True if both lists are equal in length and elements, otherwise False."""
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Append all elements of the second list to the end of the first list."""
    for num in list2:
        list1.append(num)