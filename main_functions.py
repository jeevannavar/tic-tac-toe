def new_board():
    '''
    This function creates a list of lists of shape (3,3) containing " "s, single spaces
    Inputs:
        None
    Outputs:
        list of lists of size (3,3)
    '''
    empty_board = [[" "]*3 for _ in range(3)]
    return empty_board

# print(new_board())

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
    print("|", board[0][0].center(5), "|", board[0][1].center(5), "|", board[0][2].center(5), "|")
    print("|", " "*5, "|", " "*5, "|", " "*5, "|")
    print("—"*25)
    print("|", " "*5, "|", " "*5, "|", " "*5, "|")
    print("|", board[1][0].center(5), "|", board[1][1].center(5), "|", board[1][2].center(5), "|")
    print("|", " "*5, "|", " "*5, "|", " "*5, "|")
    print("—"*25)
    print("|", " "*5, "|", " "*5, "|", " "*5, "|")
    print("|", board[2][0].center(5), "|", board[2][1].center(5), "|", board[2][2].center(5), "|")
    print("|", " "*5, "|", " "*5, "|", " "*5, "|")
    print("—"*25)

    return None

#board = new_board()
#board[1][1] = "X"
#board[2][0] = "O"
#render_board(board)

def get_move():
    '''
    This function ...
    Input:
        None
    Output:
        move = int in the range of 1 through 9
    '''
