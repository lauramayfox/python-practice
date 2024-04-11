import random
import time
import os
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
        Try to beat your highest score!
        ''')

    return player


def get_player_name():
    """
    A function to get the player's name and
    ensure only letters used.
    """

    while True:
        name = input("What is you name?: ")

        if name.isalpha():
            return name
        else:
            print("You can only use letters, please try again")

def view_scoreboard(player):
    """
    A function to view previous high scores
    """
    while True:

        view_scoreboard = input("Would you like to view previous highest score? y or n: ")

        if view_scoreboard == "y":
            print("Your highest score is:", load_high_score())
            time.sleep(1)
            break
        elif view_scoreboard == "n":
            print("\nContinue to game...")
            start_game(player)
        else:
            print("\nPlease answer y or n: \n")

def start_game(player):
    """
    A function to check if the user is ready to start the game
    """
    while True:

        start_answer = input("Start new game select y or n: ")

        if start_answer == "y":
            print("\nLets roll...")
            time.sleep(1)
            break
        elif start_answer == "n":
            print("\nSee you on the next roll")
            quit()
        else:
            print("\nPlease answer y or n: \n")

def play_game(player):
    roll_again = "y"
    score = 0
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
            score += 1 
        else:
            print("Keep trying")
    
    
    
        roll_again = input("Roll the dice again? y/n \n")
        if roll_again == "n":
            print("See you on the next roll!")
            print(f"Your total score this game: {score}")
            save_high_score(score)
            quit()        

# Adaption from Quora questions and answers on scoreboard trackers
def save_high_score(score): 
    """
    Saves the highest scores to an external text file
    """
    with open("high_score.txt", "w") as file: 
        file.write(str(score)) 
 
 
def load_high_score(): 
    """
    Gives an option to view previous high scores when game starts
    """
    if os.path.exists("high_score.txt"): 
        with open("high_score.txt", "r") as file: 
            return int(file.read()) 
    else: 
        return 0

def main():
    
    player = welcome_msg()
    view_scoreboard(player)
    start_game(player)
    play_game(player)
    load_high_score()
    

 
main()  