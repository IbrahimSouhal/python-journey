import random

secret = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("Correct! You are a genius.")
elif guess < secret:
    print("Too low! Try again.")
else:
    print("Too high! Try again.")