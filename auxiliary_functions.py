 ## This file contains auxiliary_functions for the game. 
 ## These functions are not necessary for the game, but they make the game nicer.
 ## Also, these functions are called in 1v1.py. So to play without this, remove the function calls.

class bcolours:
    """
    This class just contains the ANSI escape sequences for different colours 
    and font formatting.
    """
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    ITALIC    = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK     = '\033[5m'
    BLINK2    = '\033[6m'
    SELECTED  = '\033[7m'

    BLACK  = '\033[30m'
    RED    = '\033[31m'
    GREEN  = '\033[32m'
    YELLOW = '\033[33m'
    BLUE   = '\033[34m'
    VIOLET = '\033[35m'
    BEIGE  = '\033[36m'
    WHITE  = '\033[37m'

    BLACKBG  = '\033[40m'
    REDBG    = '\033[41m'
    GREENBG  = '\033[42m'
    YELLOWBG = '\033[43m'
    BLUEBG   = '\033[44m'
    VIOLETBG = '\033[45m'
    BEIGEBG  = '\033[46m'
    WHITEBG  = '\033[47m'

    GREY    = '\033[90m'
    RED2    = '\033[91m'
    GREEN2  = '\033[92m'
    ORANGE  = '\033[93m'
    BLUE2   = '\033[94m'
    PURPLE  = '\033[95m'
    CYAN    = '\033[96m'
    WHITE2  = '\033[97m'

    GREYBG    = '\033[100m'
    REDBG2    = '\033[101m'
    GREENBG2  = '\033[102m'
    YELLOWBG2 = '\033[103m'
    BLUEBG2   = '\033[104m'
    VIOLETBG2 = '\033[105m'
    BEIGEBG2  = '\033[106m'
    WHITEBG2  = '\033[107m'

"""
print(f"{bcolours.ORANGE}Orange{bcolours.ENDC}")
print(f"{bcolours.PURPLE}Purple{bcolours.ENDC}")
print(f"{bcolours.BLUE}Blue{bcolours.ENDC}")
print(f"{bcolours.GREEN}Green{bcolours.ENDC}")
print(f"{bcolours.CYAN}Cyan{bcolours.ENDC}")
print(f"{bcolours.RED}Red{bcolours.ENDC}")
print(f"{bcolours.BOLD}Bold{bcolours.ENDC}")
print(f"{bcolours.UNDERLINE}Underline{bcolours.ENDC}")
"""

def get_names():
    """
    This function prompts the players to enter their names
    Input:
        None
    Output:
        names = list of two strings
    """
    print(f"{bcolours.BLUE}Enter name for player 1:{bcolours.ENDC}\n")
    player_1 = str(input()).strip()
    print()
    while True:
        print(f"{bcolours.BLUE}Enter name for player 2:{bcolours.ENDC}\n")
        player_2 = str(input()).strip()
        if player_1 == player_2:
            print(f"\n{bcolours.RED}Error! Please enter a different name.{bcolours.ENDC}")
        else:
            break
    names = [player_1, player_2]

    return names

def celebrate():
    """
    This function prints a random line of celebration
    Input:
        None
    Output:
        None
    """
    with open("celebratory_lines.txt") as f:
        lines = f.readlines()
    
    from random import choice
    print(bcolours.ORANGE+choice(lines)+bcolours.ENDC)

    return None