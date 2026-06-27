
import random
print("Introduction:
This is a Python program in which the computer randomly chooses a number between1 and 100. The player has to guess the correct number. After each guess, the
program gives hints such as Too High, Too Low, or Near until the correct
number is found.")

x = random.randint(1,100)

while True:

    y = int(input("entre your guess no:"))

    if x == y-2:
        print("you are bit lower")

    elif x == y-1:
        print("you are near")

    elif x == y+1:
        print("you are near")

    elif x == y+2:
        print("you are bit higher")

    elif x < y:
        print("you are too high")

    elif x > y:
        print("you are too low")

    else:
        print("you done it!")
        break