import random
import time
# ● ┌ ─ ┐ │ └ ┘ Dice pieces for welcome message


def welcome_msg():
    """
    Welcome message to greet the player and explain the rules.
    """
    print("")
    print("┌ ─  - ┐")
    print("| ●    |")
    print("|    ● |")
    print("└ - -  ┘")
    print("*** Welcome To Dice Roll ***")
    print("┌ ─  - ┐")
    print("| ●    |")
    print("|    ● |")
    print("└ - -  ┘\n")
    
    player = get_player_name()

    print(f"\nAlright, {player} the rules for this game are:")
    print(
        '''
        The aim is to roll the highest value...
        You will take turns against the computer...
        The highest score wins!
        ''')

    return player

def get_player_name():
    """
    A function to get the players name and
    validate that it is only letters used.
    """

    while True:
        name = input("What is you name?: ")

        if name.isalpha():
            return name
        else:
            print("You can only use letters, please try again")

def start_game(player):
    """
    A function to check if the user is ready to start the game
    """
    while True:

        start_answer = input("Start new game press y or n: ")

        if start_answer == "y":
            print("\nLets roll...")
            break
        elif start_answer == "n":
            print("\nSee you on the next roll")
            break
        else:
            print("\nPlease answer y or n\n")



player = welcome_msg()
start_game(player)
