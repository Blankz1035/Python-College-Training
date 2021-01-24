# Program to simulate the game "Sixes Bet".
# Sixes Bet is an old dice game. The bet is simple: will the player roll a 6 at least once out of four rolls?

# The program should allow the player to roll the die up to
# 4 times, display the roll, and check if the player has rolled a six. If the player has rolled a 6, the
# game is over and the player has won. If the player rolls 4 times and hasn't rolled a 6, s/he loses.

# Inports
from random import randint

count = 0

while count < 4:
    count += 1

    input("Press 'Enter' to roll the dice")
    roll = randint(1,6)

    print(f"User rolled a {roll} !")

    if roll == 6:
        print("Player wins! 6 has been rolled.")
        break

    if count == 4:
        print(f"You have lost the game! {count} rolls done. ")

