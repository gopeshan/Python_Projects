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

    # Determine the winner
    if (user_choice == 'R' and comp_choice == 'P') or \
       (user_choice == 'P' and comp_choice == 'S') or \
       (user_choice == 'S' and comp_choice == 'R'):
        comp_score += 1
    elif (user_choice == 'P' and comp_choice == 'R') or \
         (user_choice == 'S' and comp_choice == 'P') or \
         (user_choice == 'R' and comp_choice == 'S'):
        user_score += 1
    else:
        print("It's a tie!")

    # Display current score
    print("\nSCORE:")
    print("Your Score:", user_score, "\tComputer Score:", comp_score, "\n")

# Display final score
print("\n\t\tFINAL SCORE:")
print("Your Score:", user_score, "\t\t\tComputer Score:", comp_score, "\n")

# Determine the overall winner
if user_score > comp_score:
    print("\n\tCongratulations! You Won!")
elif user_score < comp_score:
    print("\n\t\tYou Lost!")
else:
    print("\n\t\tIt's a Tie!")
