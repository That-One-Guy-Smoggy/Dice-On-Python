# Multiple dice made within python
# Program fully developed by Smoggy


import random
import time

min_range = 1
max_range = 6


diceRolls = int(input("How many dice do you want to roll: "))
lmao = input("Are you ready to roll the dice? (Y/N): ")

# Main "dice"/program
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


# Fully developed by Smoggy
# Twitter --- @Smoggy445
# Github --- @That-One-Guy-Smoggy

# Notes:
# I know this is not the most optimal set up, or maybe it is I don't really know as this is like the fourth or fifth
# program I make. Please be respectful, I am a year 10 student who started learning Python over summer, mainly for fun
# and to have an easier time on my current year group (Year 10). Thanks for viewing my program.
#
# I would really like feedback thank you! :)
