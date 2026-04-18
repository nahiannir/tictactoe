# create a list of 9 empty spaces to represent the board
board = [' ' for _ in range(9)]

# function to print the current board in a 3x3 format
def print_board():
    print() #  Print empty line for spacing
    print(board[0] + ' | ' + board[1] + ' | ' + board[2]) # first row 
    print('--+---+--') # separator line
    print(board[3] + ' | ' + board[4] + ' | ' + board[5]) # second row
    print('--+---+--') # separator line
    print(board[6] + ' | ' + board[7] + ' | ' + board[8]) # third row
    print() #  Print empty line for spacing

# function to check if the player has won the game
def check_winner(player):
    # list of all winning combinations
    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8], # rows winning combinations
        [0,3,6], [1,4,7], [2,5,8], # columns winnning combinations
        [2,4,6], [0,4,8], # diagonals winning combinations
    ]

    # loop through each winning winning_combinations
    for combination in winning_combinations:
        # check if all positions in that combinations match the player
        if all(board[i] == player for i in combination):
            return True  # the player has owon
        return False # the player lost
    
# function to check if the game was a draw
def is_draw():
    # if there are no empty spaces left its a draw
    return ' ' not in board

# main func to control the game flow
def play_game():
    current_player = 'X' # X always starts first

    # infinite loops until game ends
    while True:
        print_board() # show the board

        try:
            # ask input 1-9 and covert to 0-8 Index 
            move = int(input(f'Player {current_player}, choose position between 1-9: ')) - 1
            # check if the move is valid
            if move < 0 or move > 8 or board[move] != ' ':
                print('Invalid move. Try again.') # error message
                continue # skips for next loop

            # place the players moves 
            board[move] = current_player

            # check if the current player has won
            if check_winner(current_player):
                print_board() # show the final board
                print(f'Player {current_player} wins!') # win message
                break # exit the loop
            # check if the game is a draw
            if is_draw():
                print_board() # show the final board 
                print('It\'s a draw!') # draw message
                break # exit the loop
            # switch player ( x to  o or o to x)
            current_player = 'O' if current_player == 'X' else 'X'
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 9.') # error message for non-integer input

# start game by calling function 
play_game()