import random

# Draw a random number between 1 and 10
number_to_guess = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess < number_to_guess:
        print("Too low.")
    elif guess > number_to_guess:
        print("Too high.")
    else:
        print("Correct! You guessed the number.")
        break