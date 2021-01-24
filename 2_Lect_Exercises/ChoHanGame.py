# Program to simulate the game of ChoHan.  - Andy Blankley
# Objective: Game must be able to take in a player guess, generate 2 random dice rolls and inform the user of the result.

# Inports
from random import randint

# Inputs
player_guess = input("Enter your guess (even or odd): ")
# Processing / Validations
player_guess = player_guess.lower()

if player_guess != "even" and player_guess != "odd":
    print("Player input not valid.")
else:
    # Simulate dice roll
    dice_roll1 = randint(1, 6)
    dice_roll2 = randint(1, 6)
    total = dice_roll1 + dice_roll2

    print(f"Dice rolls: {dice_roll1} and {dice_roll2} gives total: {total}.")
    # Check result and print result
    if (total % 2 == 0 and player_guess == "even") or (total % 2 != 0 and player_guess == "odd"):
        print("You guessed correctly!")
    else:
        print("Incorrect guess!")

