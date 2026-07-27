import random

def guess_game():
    number = random.randint(1, 100)
    attempts = 0

    print("Guess a number between 1 and 100")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess > number:
                print("Too high!")
            elif guess < number:
                print("Too low!")
            else:
                print("Correct!")
                print("You guessed it in", attempts, "attempt(s).")
                break

        except ValueError:
            print("Please enter a valid number.")

while True:
    guess_game()

    choice = input("Do you want to play again? (yes/no): ").lower()

    if choice != "yes":
        print("Thanks for playing!")
        break