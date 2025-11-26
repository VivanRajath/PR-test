# Number Guessing Game

import random

secret = random.randint(1, 50)
attempts = 0

print("===== Number Guessing Game =====")
print("Guess a number between 1 and 50")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret:
        print("Correct! You guessed the number in", attempts, "attempts")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
