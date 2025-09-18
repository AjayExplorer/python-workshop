# Simple Python Program: Guess the Number 🎯

# Importing the random module to generate a random number
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Welcome to the Guessing Game!")
print("I am thinking of a number between 1 and 10.")

# Give the user 3 chances
for attempt in range(3):
    # Take input from user
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

else:
    print(f"😢 Sorry, you're out of attempts. The number was {secret_number}.")
