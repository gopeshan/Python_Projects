import random

# Default values
choices = {'R': "Rock", 'P': "Paper", 'S': "Scissors"}
user_score = 0
comp_score = 0

# Input number of games to play
total_games = int(input("Enter the number of games you want to play: "))

# Game loop
while comp_score + user_score < total_games:
    # User input
    user_choice = input("\nYour choice (R/P/S): ").upper()

    # Check for valid input
    if user_choice not in choices:
        print("Invalid input. Please enter R, P, or S.")
        continue

    # Computer choice
    comp_choice = random.choice(list(choices.keys()))

    print("Computer's choice: ", choices[comp_choice])

    
