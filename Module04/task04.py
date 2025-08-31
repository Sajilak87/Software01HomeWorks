import random

# Computer draws a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Guess the number (between 1 and 10)!")

while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Correct! You guessed it!")
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")