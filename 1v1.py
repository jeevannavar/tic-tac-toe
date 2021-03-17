# This file contains code to play a simple game between two humans using the same terminal
from main_functions import *
from auxiliary_functions import *

# The outer while loop is so that players can start another game without exiting the script
while True:
    board = new_board() 
    layout = [['1','2','3'],['4','5','6'],['7','8','9']]

    print(f"\n{bcolours.BOLD}{bcolours.PURPLE}TIC TAC TOE !!{bcolours.ENDC}\n")
    print("This is the layout of the board.")
    render_board(layout)
    print("")

    players = get_names()
    current_player = players[0]
    markers = dict(zip(players, ["X", "O"]))
    moves = 0

    while True:
        print()
        print(f"{bcolours.GREEN}{current_player}{bcolours.ENDC}")
        coords = get_move(board)

        marker = markers[current_player]
        board = make_move(board, marker, coords)
        moves += 1

        render_board(board)

        if winner(board):
            print(f"{bcolours.RED}Game Over!{bcolours.ENDC}")
            print(f"{bcolours.GREEN}{current_player}{bcolours.ENDC} is the winner!")
            celebrate()
            break

        if isBoardFull(board):
            print(f"{bcolours.RED}Game Over!{bcolours.ENDC}\nThe game is a draw.\n")
            break

        #Switching players at the end of the turn
        current_player = players[moves%2]

    print(f"{bcolours.BLUE}Would you like to play again?\nEnter <Yes> to play again.{bcolours.ENDC}")
    if input().strip().lower() == "yes":
        print("_"*100)
        continue
    else:
        break