import random

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