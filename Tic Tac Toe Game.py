players = 'XO'
board = '''
  0   1   2
  {0} | {1} | {2}
 -----------
3 {3} | {4} | {5} 5
 -----------
  {6} | {7} | {8}
  6   7   8
'''
win_conditions = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontals
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # verticals
    (0, 4, 8), (2, 4, 6)              # diagonals
]

def check_win(player, squares):
    for a, b, c in win_conditions:
        if {squares[a], squares[b], squares[c]} == {player}:
            return True
    return False

def print_board(squares):
    print(board.format(*squares))

while True:
    squares = [' ']*9  # Reset the board for each game
    print("Welcome to Tic-Tac-Toe!")
    print_board(squares)

    while ' ' in squares:
        move = input(f'{players[0]} to move [0-8] > ')
        if not move.isdigit() or not 0 <= int(move) <= 8 or squares[int(move)] != ' ':
            print('Invalid move!')
            continue

        squares[int(move)], players = players[0], players[::-1]
        print_board(squares)

        if check_win(players[1], squares):
            print(f'{players[1]} is the winner!')
            break

    if ' ' not in squares:
        print('Cats game!')

    play_again = input('Do you want to play again? (yes/no): ')
    if play_again.lower() != 'yes':
        break

