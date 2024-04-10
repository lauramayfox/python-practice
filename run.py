import random
import time
# ● ┌ ─ ┐ │ └ ┘ Dice pieces for welcome message


def welcome_msg():
    """
    Welcome message to greet the player and explain the rules.
    """
    print("")
    print("┌ ─  - ┐  ┌ ─  - ┐")
    print("| ●    |  | ●    |")
    print("|    ● |  |    ● |")
    print("└ - -  ┘  └ - -  ┘")
    print("*** Welcome To Double Dice ***")
    print("┌ ─  - ┐  ┌ ─  - ┐")
    print("| ●    |  | ●    |")
    print("|    ● |  |    ● |")
    print("└ - -  ┘  └ - -  ┘\n")
    
    player = get_player_name()

    print(f"\nAlright, {player} the rules for this game are:")
    print(
        '''
        The aim is to roll 2 of the same numbers...
        Double or nothing...
        Good luck!
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
            time.sleep(1)
            break
        elif start_answer == "n":
            print("\nSee you on the next roll")
            quit()
        else:
            print("\nPlease answer y or n\n")

def play_game(player):
    roll_again = "y"
    while roll_again == "y":
        print("Rolling the dice...")
        time.sleep(1)

        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print("The values are: ")
        print("Dice 1 =", dice1)
        print("Dice 2 =", dice2)

        if dice1 == dice2:
            print("You rolled a double! You win!")
        else:
            print("Keep trying")
    
        roll_again = input("Roll the dice again? y/n \n")
        if roll_again == "n":
            print("See you on the next roll!")
            print("Your total score this game: ")
            quit()        

def main():
    player = welcome_msg()
    start_game(player)
    play_game(player)

 
main()  