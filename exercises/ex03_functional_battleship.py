"""This is my EX03 Functional Battleship."""
__author__ = "730668694"
import random


BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U00002B1C"


def input_guess(grid_size: int, row_or_column: str) -> int:
    """Prompts the user for a row or column guess within the grid size bounds."""
    assert row_or_column == "row" or row_or_column == "column", f"Invalid input: {row_or_column}. Must be 'row' or 'column'."

    while True:
        user_input = input(f"Guess a {row_or_column}: ")
        try:
            guess = int(user_input)
            if 1 <= guess <= grid_size:
                return guess
            else:
                print(f"The grid is only {grid_size} by {grid_size}. Try again.")
        except ValueError:
            print("Please enter a valid integer.")


def print_grid(grid_size: int, guess_row: int, guess_col: int, is_correct: bool) -> None:
    """Print the game board grid."""
    row = 1
    while row <= grid_size:
        col = 1
        while col <= grid_size:
            if row == guess_row and col == guess_col:
                print(RED_BOX if is_correct else WHITE_BOX, end="")
            else:
                print(BLUE_BOX, end="")
            col += 1
        print()  # New line after each row
        row += 1


def correct_guess(secret_row: int, secret_col: int, guess_row: int, guess_col: int) -> bool:
    """Determine if the guess is correct."""
    return secret_row == guess_row and secret_col == guess_col


def main(grid_size: int, secret_row: int, secret_col: int) -> None:
    """Manage the main gameplay loop of Battleship with specified grid size and secret ship location."""
    turn = 1
    max_turns = 5
    while turn <= max_turns:
        print(f"=== Turn {turn}/{max_turns} ===")
        guess_row = input_guess(grid_size, "row")
        guess_col = input_guess(grid_size, "column")
        is_correct = correct_guess(secret_row, secret_col, guess_row, guess_col)
        print_grid(grid_size, guess_row, guess_col, is_correct)
        if is_correct:
            print(f"Hit! You won in {turn}/{max_turns} turns!")
            return
        else:
            print("Miss!")
        turn += 1
    print(f"X/{max_turns} - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))