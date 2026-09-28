import random

num = random.randint(1, 11)

tries = 0

while True:
    guess = int(input("Guess a number: "))

    tries += 1

    if num == guess:
        print("You win Konika")
        print(f"You tried {tries} times")
        break

    elif num < guess:
        print("Go lower")

    elif num > guess:
        print("Go higher")