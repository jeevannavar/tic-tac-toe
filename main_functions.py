## This file contains the main functions required for playing a simple game of tic-tac-toe in the terminal

def new_board():
    '''
    This function creates a list of lists of shape (3,3) containing " "s, single spaces
    Inputs:
        None
    Outputs:
        list of lists of size (3,3)
    '''
    empty_board = [["     "]*3 for _ in range(3)]
    return empty_board


def render_board(board):
    '''
    This function takes a 3x3 board as input and prints it to console
    Input:
        board   = list of lists of size (3,3)
    Output:
        None
    '''
    print("_"*25)
    print("|", " "*5, "|", " "*5, "|", " "*5, "|")
    print("|", board[0][0], "|", board[0][1], "|", board[0][2], "|")
    print("|", " "*5, "|", " "*5, "|", " "*5, "|")
    print("—"*25)
    print("|", " "*5, "|", " "*5, "|", " "*5, "|")
    print("|", board[1][0], "|", board[1][1], "|", board[1][2], "|")
    print("|", " "*5, "|", " "*5, "|", " "*5, "|")
    print("—"*25)
    print("|", " "*5, "|", " "*5, "|", " "*5, "|")
    print("|", board[2][0], "|", board[2][1], "|", board[2][2], "|")
    print("|", " "*5, "|", " "*5, "|", " "*5, "|")
    print("—"*25)

    return None


def get_move(board):
    '''
    This function ...
    Input:
        board   = current state of the board
    Output:
        move    = int in the range of 1 through 9
    '''
    print("Choose the tile you would like to mark: (Enter number between 1 and 9)")
    valid_moves = [i+1 for i in range(9) if board[i//3][i%3] == "     "] # List of valid moves
    try:
        move = int(input())
        assert move in valid_moves
    except:
        print("\nInvalid move! Try again!")
        move = get_move(board)

    return move


def make_move(board, marker, coords):
    '''
    This function makes the move on the board.
    Currently it can take only fixed player names and has fixed player markers.
    Input:
        board           = list of lists of size (3,3)
        marker          = str, either "X" or "O"
        move            = int in the range of 1 through 9
    Output:
        board           = list of lists of size (3,3)
    '''
    coords -= 1         #This is to bring the coordinate to zero indexing
    board[coords//3][coords%3] = marker

    return board


def winner(board):
    '''
    This function checks if a winner can be declared
    Input:
        board   = list of lists of size (3,3)
    Output:
        winner  = boolean, True if winner can be declared
    '''
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "     ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "     ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "     ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "     ":
        return True

    return False


def isBoardFull(board):
    '''
    This function checks if the board if full
    Input:
        board       = list of lists of size (3,3)
    Output:
        fullness    = boolean, True if the board is full
    '''
    if any("     " in row for row in board):
        return False
    return True