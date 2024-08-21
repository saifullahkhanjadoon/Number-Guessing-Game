import random

secret_number = random.randint(1, 100)


max_attempts = 10
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"You have 10 attempts to guess the correct number.")


while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
        break  

if attempts == max_attempts and guess != secret_number:
    print(f"Sorry, you've used all your attempts. The correct number was {secret_number}.")

print("Thank you for playing!")
