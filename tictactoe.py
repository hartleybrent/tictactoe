# Simple Tic Tac Toe game. #
# Brent Hartley Udemy Python course #
import random
# Define game functions #
def display_board(board):
    # Space new board in shell #
    print("\n")
    print("\n")
    # Empty board template #
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
# Let First player decide to be X's or O's #
def player_select():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
# Check for win #
def place_marker(board, marker, position):
    board[position] = marker
# See if board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
    # Check for a win #
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 
# Randomly choose first player #
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
# Play again? #
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
# Let player choose position #
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position
def space_check(board, position):
    return board[position] == ' '
# Run the game #
print('Welcome to Tic Tac Toe!')
while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_select()
    turn = choose_first()
    print(turn + ' will go first.')
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break