"""EX01 - Simple Battleship - This is a step towards the simple battleship."""

__author__ = "730668694"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

player1_ship_location: int = int(input("Pick a secret boat location between 1 and 4: "))

if player1_ship_location < 1:
    print("Error! " + str(player1_ship_location) + " too low!")
    exit()
elif player1_ship_location > 4:
    print("Error! " + str(player1_ship_location) + " too high!")
    exit()

player2_guess_location: int = int(input("Guess a number between 1 and 4: "))

if player2_guess_location < 1:
    print("Error! " + str(player2_guess_location) + " too low!")
    exit()
elif player2_guess_location > 4:
    print("Error! " + str(player2_guess_location) + " too high!")
    exit()

if player1_ship_location == player2_guess_location:
    result = RED_BOX
    print("Correct! You hit the ship.")
elif player1_ship_location != player2_guess_location:
    result = WHITE_BOX
    print("Incorrect! You missed the ship.")

emoji_string: str = ""

if player2_guess_location == 1:
    emoji_string += result
else:
    emoji_string += BLUE_BOX

if player2_guess_location == 2:
    emoji_string += result
else:
    emoji_string += BLUE_BOX

if player2_guess_location == 3:
    emoji_string += result
else:
    emoji_string += BLUE_BOX

if player2_guess_location == 4:
    emoji_string += result
else:
    emoji_string += BLUE_BOX

print(emoji_string)
