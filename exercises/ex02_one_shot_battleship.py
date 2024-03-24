"""EX02 One Shot battleship due 02/06."""

__author__ = "730668694"

BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U00002B1C"

# Grid and secret coordinates
GRID_SIZE = 4
SECRET_ROW = 3
SECRET_COLUMN = 2

# Get row guess
while True:
    guess_row_input = input("Guess a row: ")
    try:
        guess_row = int(guess_row_input)
        if 1 <= guess_row <= GRID_SIZE:
            break
        else:
            print(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: ", end="")
    except ValueError:
        print("Enter a valid integer. Try again: ", end="")

# Get column guess
while True:
    guess_column_input = input("Guess a column: ")
    try:
        guess_column = int(guess_column_input)
        if 1 <= guess_column <= GRID_SIZE:
            break
        else:
            print(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: ", end="")
    except ValueError:
        print("Enter a valid integer. Try again: ", end="")

# Determine the result box
result_box = RED_BOX if guess_row == SECRET_ROW and guess_column == SECRET_COLUMN else WHITE_BOX

# Display the grid using while loops
current_row = 1
while current_row <= GRID_SIZE:
    row_string = ""
    current_col = 1
    while current_col <= GRID_SIZE:
        if current_row == guess_row and current_col == guess_column:
            row_string += result_box
        else:
            row_string += BLUE_BOX
        current_col += 1
    print(row_string)
    current_row += 1

# Feedback to the player
if guess_row == SECRET_ROW and guess_column == SECRET_COLUMN:
    print("Hit!")
elif guess_row == SECRET_ROW:
    print("Close! Correct row, wrong column.")
elif guess_column == SECRET_COLUMN:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")