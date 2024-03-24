""""Number guessing game"""

from random import randint

SECRET: int = randint(1,10)
correct: bool = False



while correct == False:
    guess: int = int(input("Guess a number: "))

    if guess > 10:
        print("Error!, Number is too high, try again")
    elif guess < 1:
        print("Error, Number is too low, try again")
    

    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number")
        correct = True
    else:
        print(f"you got it wrong {guess} is not right")

