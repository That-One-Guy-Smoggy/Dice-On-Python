import random
import time

min_range = 1
max_range = 6


diceRolls = int(input("How many dice do you want to roll: "))
lmao = input("Are you ready to roll the dice? (Y/N): ")

while lmao == "Y":
    if diceRolls == 1:
        print("Your the dice said that your number is")
        print(random.randrange(min_range, max_range))
        lmao = input("Would you like to roll the dice again? (Y/N)")
    elif diceRolls > 1:
        print("Your numbers are")
        for i in range(diceRolls):
            time.sleep(.5)
            print(random.randrange(min_range, max_range))
        lmao = input("Would you like to roll the dice again? (Y/N)")
    elif lmao == "N":
        print("Then why did you run the program in the first place?")
    else:
        print("Press any key to exit")
else:
    print("You're free to exit")

