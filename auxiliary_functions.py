 ## This file contains auxiliary_functions for the game. 
 ## These functions are not necessary for the game, but they make the game nicer.
 ## Also, these functions are called in 1v1.py. So to play without this, remove the function calls.

def get_names():
    """
    This function prompts the players to enter their names
    Input:
        None
    Output:
        names = list of two strings
    """
    print("Enter name for player 1:\n")
    player_1 = str(input()).strip()
    print()
    while True:
        print("Enter name for player 2:\n")
        player_2 = str(input()).strip()
        if player_1 == player_2:
            print("\nError! Please enter a different name.")
        else:
            break
    names = [player_1, player_2]

    return names
