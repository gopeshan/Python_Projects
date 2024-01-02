import random

def guess_number_game():
    print("Welcome to the Number Guessing Game!")

    # Generate a random number between 1 and 9
    target_number = random.randint(1, 9)

    # Set the maximum number of attempts
    max_attempts = 5
    attempts = 0

    print("Guess a number between 1 and 9:")

    # Loop to allow the user to guess the number
    while attempts < max_attempts:
        user_guess = int(input("Enter your guess: "))

        if user_guess == target_number:
            print(f'Congratulations! You guessed the number {target_number} in {attempts + 1} attempts!')
            break
        elif user_guess < target_number:
            print("Your guess was too low. Try a higher number.")
        else:
            print("Your guess was too high. Try a lower number.")

        attempts += 1

    # Inform the user if they couldn't guess the number
    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {target_number}.")

# Run the game
guess_number_game()
