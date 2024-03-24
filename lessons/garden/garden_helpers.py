"""Some functions for my Garden Plan!"""

__author__ = "730668694"


def add_by_kind(garden_by_category: dict[str, list[str]], category: str, plant: str) -> None:
    """Adds a plant to a dictionary sorted by its category (e.g., flower, vegetable)."""
    if category in garden_by_category:
        garden_by_category[category].append(plant)
    else:
        garden_by_category[category] = [plant]


def add_by_date(garden_by_time: dict[str, list[str]], sowing_month: str, plant: str) -> None:
    """Adds a plant to a dictionary sorted by its sowing month."""
    if sowing_month in garden_by_time:
        garden_by_time[sowing_month].append(plant)
    else:
        garden_by_time[sowing_month] = [plant]


def look_up_by_kind_and_date(category_plants: dict[str, list[str]], time_plants: dict[str, list[str]], desired_category: str, desired_month: str) -> str:
    """Determines which plants from a specified category can be planted in a given month."""
    plants_to_plant = [plant for plant in category_plants.get(desired_category, []) 
                     if plant in time_plants.get(desired_month, [])]

    if plants_to_plant:
        return f"{desired_category}s to plant in {desired_month}: {plants_to_plant}."
    else:
        return f"No {desired_category}s to plant in {desired_month}."