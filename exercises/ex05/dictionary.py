"""EX05 - Dictionary Utility Functions."""


__author__ = '730668694'


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary by swapping its keys and values, raising an error if duplicate values are encountered."""
    dict2: dict[str, str] = {}

    for key, value in dict1.items():
        if value in dict2:
            raise KeyError(f"Duplicate key encountered: {value}")
        dict2[value] = key
   
    print(dict2)
    return dict2


def favorite_color(dict1: dict[str, str]) -> str:
    """Returns the most popular color from a dictionary of names and their favorite colors."""
    dict2: dict[str, int] = {}  # Counts occurrences of each color

    for value in dict1.values():
        if value in dict2:
            dict2[value] += 1
        else:
            dict2[value] = 1

    max_count: int = 0
    favorite: str = ""

    for key, value in dict1.items():
        if dict2[value] > max_count or (dict2[value] == max_count and favorite == ""):
            max_count = dict2[value]
            favorite = value

    return favorite


print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))


def count(dict1: list[str]) -> dict[str, int]:
    """Produces a dictionary with counts of each unique value in the given list."""
    dict2: dict[str, int] = {}

    for value in dict1:
        if value in dict2:
            dict2[value] += 1
        else:
            dict2[value] = 1

    return dict2


def alphabetizer(dict1: list[str]) -> dict[str, list[str]]:
    """Categorizes words in dict1 into lists based on their starting letter."""
    dict2: dict[str, list[str]] = {}

    for value in dict1:
        key = value[0].lower()
        if key not in dict2:
            dict2[key] = []
        dict2[key].append(value)

    return dict2


def update_attendance(attendance_log: dict[str, list[str]], day: str, name: str) -> None:
    """Updates the attendance log with a new entry, avoiding duplicates."""
    if day in attendance_log:
        if name not in attendance_log[day]:
            attendance_log[day].append(name)
    else:
        attendance_log[day] = [name]


attendance_log = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
update_attendance(attendance_log, "Tuesday", "Vrinda")
update_attendance(attendance_log, "Wednesday", "Kaleb")
print(attendance_log)