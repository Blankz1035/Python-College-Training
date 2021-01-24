# Program that randomly selects a number between 1 and 15, and then repeatedly (up to 10 times)
# by Andy Blankley

from random import randint

## Generate Random Number
randomnumber = randint(1, 15)
print("Random number selected.\n")
control = 0

# Function created for reusability in both winning and loosing scenarios
def newgame():
    while True:
        playagain =  input("Would you like to play again: y/n? ").lower()
        if playagain == "y":
            global randomnumber
            
            randomnumber = randint(1, 10)
            print("Random number selected.")
            return 0

        elif playagain == "n":
            return 10
        else:
            print("Incorrect answered entered.")
    
while (control < 10):
    guess = int(input("Enter your guess: "))

    if guess < randomnumber:
        print("Guess is too lower.")
    elif guess > randomnumber:
        print("Guess is too higher.")
    else:
        print("You guessed correctly!")
        control = newgame()
 
    control += 1

    if control == 10:
        print("You loose!")
        control = newgame()





