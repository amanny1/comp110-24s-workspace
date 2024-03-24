"""Test my garden functions."""

__author__ = "730668694"


from lessons.garden.garden_helpers import add_by_kind, add_by_date, look_up_by_kind_and_date


def test_add_plant_by_category_edge_case():
    """Test adding a plant to an empty category-based garden dictionary."""
    garden = {}
    add_by_kind(garden, "flower", "daisy")
    assert garden == {"flower": ["daisy"]}


def test_add_plant_by_category_use_case():
    """Test adding a plant to an existing category in the category-based garden dictionary."""
    garden = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(garden, "flower", "daisy")
    assert garden == {"flower": ["marigold", "zinnia", "daisy"], "vegetable": ["carrots"]}


def test_add_plant_by_planting_time_edge_case():
    """Test adding a plant to an empty month-based garden dictionary."""
    garden = {}
    add_by_date(garden, "April", "daisy")
    assert garden == {"April": ["daisy"]}


def test_add_plant_by_planting_time_use_case():
    """Test adding a plant to an existing month in the month-based garden dictionary."""
    garden = {"April": ["marigold"], "June": ["carrots"]}
    add_by_date(garden, "April", "daisy")
    assert garden == {"April": ["marigold", "daisy"], "June": ["carrots"]}


def test_looking_up_by_kind_and_date_edge_case():
    """Test looking up plants to plant where none match the criteria."""
    category_plants = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    time_plants = {"April": ["marigold"], "June": ["carrots"]}
    result = look_up_by_kind_and_date(category_plants, time_plants, "flower", "June")
    assert result == "No flowers to plant in June."

def test_looking_up_by_kind_and_date_use_case():
    """Test finding plants to plant that match both the category and the planting month."""
    category_plants = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    time_plants = {"April": ["marigold"], "June": ["carrots"]}
    result = look_up_by_kind_and_date(category_plants, time_plants, "flower", "April")
    assert result == "flowers to plant in April: ['marigold']."