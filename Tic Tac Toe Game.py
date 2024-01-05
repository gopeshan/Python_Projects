def check_win(player, squares):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontals
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # verticals
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    return any(set(squares[a] for a in line) == {player} for line in win_conditions)

def print_board(squares):
    board = '''
      0   1   2
      {0} | {1} | {2}
    -----------
    3 {3} | {4} | {5} 5
    -----------
      {6} | {7} | {8}
      6   7   8
    '''
    print(board.format(*squares))

def is_valid_move(move, squares):
    return move.isdigit() and 0 <= int(move) <= 8 and squares[int(move)] == ' '

def play_tic_tac_toe():
    players = ['X', 'O']

    while True:
        squares = [' ']*9  # Reset the board for each game
        print("Welcome to Tic-Tac-Toe!")
        print_board(squares)

        while ' ' in squares:
            move = input(f'{players[0]} to move [0-8] > ')

            if not is_valid_move(move, squares):
                print('Invalid move! Please choose a valid, unoccupied position.')
                continue

            squares[int(move)] = players[0]
            print_board(squares)

            if check_win(players[0], squares):
                print(f'{players[0]} is the winner!')
                break

            players.reverse()  # Switch players

        if ' ' not in squares:
            print('Cats game!')

        play_again = input('Do you want to play again? (yes/no): ')
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    play_tic_tac_toe()
