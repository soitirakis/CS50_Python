#guessing game

import random

while True:
    try:
        level = int(input("Level: "))
        guess = random.randrange(1,level)
        if level < 0:
            raise ValueError
        break
    except ValueError:
        continue
while True:
    try:
        user = int(input("Guess: "))
        if user < 0:
            raise ValueError
        break
    except ValueError:
        continue

while user != guess:
    if user > guess:
        print("Too large!")
    elif user < guess:
        print("Too small!")
    user = int(input("Guess: "))

print("Just right!")
