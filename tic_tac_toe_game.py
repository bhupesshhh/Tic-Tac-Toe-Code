"""
Interactive Tac-Tac-Toe game
"""

# Imports
import random
from os import system
from os import name


def clear():
    """
    This function clears up the screen.
    No inputs are taken.
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def sample_display():
    """
    This function introduces our game to users.
    No inputs are taken.
    """
    # Game Intro Display Function
    print("-------------")
    print(f"| {6} | {7} | {8} |   X-X-X-X-X-X")
    print("|-----------|")
    print(f"| {3} | {4} | {5} |   TIK-TAC-TOE")
    print("|-----------|")
    print(f"| {0} | {1} | {2} |   O-O-O-O-O-O")
    print("-------------")


def display(list1):
    """
    This function shows up the board.
    list1: takes a list with of length 9.
    """
    # Empty Board
    print("-------------")
    print(f"| {list1[6]} | {list1[7]} | {list1[8]} |")
    print("|-----------|")
    print(f"| {list1[3]} | {list1[4]} | {list1[5]} |")
    print("|-----------|")
    print(f"| {list1[0]} | {list1[1]} | {list1[2]} |")
    print("-------------")


def first_player():
    """
    This function makes decision on who goes first.
    No inputs are taken.
    """
    # Who goes first
    # Initial Value
    choice = "WRONG"

    # Loop Condition to keep asking for valid input
    while choice not in ["X", "O"]:
        # User Input
        choice = input("Enter Your Marker (X or O): ")
        # Digit Check
        if choice not in ["X", "O"]:
            print("Sorry, Invalid Marker. Pick from (X or O) only!")

    if choice == "X":
        choice2 = "O"
    else:
        choice2 = "X"

    print(f"Player 1 has {choice} marker.")
    print(f"Player 2 has {choice2} marker.\n")
    return choice, choice2


def valid_input(list1):
    """
    This function asks for inputs and check if it is valid or not.
    list1: takes a list of length 9.
    """
    # Valid User Input
    # Initial Value
    choice = "WRONG"
    within_range = False

    # Loop Condition to keep asking for valid input
    while (choice.isdigit() == False) or (within_range == False):

        # User Input
        choice = input("Enter Your Position (Only 0-8): ")

        # Digit Check
        if choice.isdigit() == False:
            print("Sorry, Invalid Input. Position (0-8) only!")
        else:
            # Range Check
            if int(choice) not in range(0, 9):
                print("Sorry, Invalid Input. Position not in range (0-8)!")
            else:
                # Check for empty space and assign within_range for valid input
                pos = int(choice)
                if list1[pos] == "X" or list1[pos] == "O":
                    print("Position already filled. Pick a new one")
                else:
                    within_range = True

    return int(choice)


def win_check(board, mark):
    """
    This function check if a playen has won or not.
    board: the list of board is taken.
    mark : the player marker is taken.
    """
    # Check for win
    return (
        (board[6] == mark and board[7] == mark and board[8] == mark) or  # across the top
        (board[3] == mark and board[4] == mark and board[5] == mark) or  # across the middle
        (board[0] == mark and board[1] == mark and board[2] == mark) or  # across the bottom
        (board[6] == mark and board[3] == mark and board[0] == mark) or  # down the middle
        (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
        (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the right side
        (board[6] == mark and board[4] == mark and board[2] == mark) or  # diagonal
        (board[8] == mark and board[4] == mark and board[0] == mark))  # diagonal


def len_list(new_list, position):
    """
    This function checks for the length of list which is saving all the inputs.
    new_list: the new list to save all the inputs
    postion: the postion where the number needs to be saved.
    """
    # Draw Check
    new_list.append(position)
    if len(new_list) == 9:
        print("All places are full. It's a draw")
        return True
    else:
        return False


def postion_update(game_list, position, marker):
    """
    This function shows the updated board.
    game_list: the list where numbers are saved.
    postion: where the marker is going to show.
    marker: the marker of the player.
    """
    # Position Update
    game_list[position] = marker
    return game_list


def game_choice():
    """
    This function gives option to the user to continue a new game.
    No inputs are taken.
    """
    # Continue Gameplay
    choice = "wrong"
    while choice not in ["Y", "N"]:
        choice = input("Keep Playing (Y or N): ")
        if choice not in ["Y", "N"]:
            print("Sorry, Invalid Choice")
    if choice == "Y":
        return True
    else:
        return False


def game_start():
    """
    This function gives option to the user to start a new game.
    No inputs are taken.
    """
    # Gameplay Start
    choice = "wrong"
    while choice not in ["Y", "N"]:
        choice = input("Would you like to play ? (Y or N): ")
        if choice not in ["Y", "N"]:
            print("Sorry, Invalid Choice")
    if choice == "Y":
        return True
    else:
        return False


# Show the game
sample_display()

# Ask for start the game
answer = game_start()
if answer == True:
    print("\nLet's start the game")
    gameplay = game_on = True
else:
    gameplay = game_on = False
    print("\nHope to see you soon!")

while game_on:

    # Pick the first Player
    print("")
    marker1, marker2 = first_player()

    game_list = [" "]*9
    number_list = []
    player = random.randint(1, 2)

    while gameplay:

        # Turn
        print(f"Player {player} Turn")
        if player == 1:
            marker = marker1
        else:
            marker = marker2

        # Valid Input
        position = valid_input(game_list)

        # Updated Board
        game_list = postion_update(game_list, position, marker)

        # Show updated board
        display(game_list)

        # Check for win
        win = win_check(game_list, marker)
        if win == True:
            # Winner Announcement
            print(f"Player {player} wins!")
            print("Thanks for playing\n")
            break

        # Check for Full Board
        fullboard = len_list(number_list, position)
        if fullboard == True:
            break

        # Change of Turn
        if player == 1:
            player = 2
        else:
            player = 1
        print("")

    # Ask to play again
    answer = game_choice()
    if answer == True:
        game_on = True
        clear()
        # Show the game
        sample_display()
        print("\nLet's start again")
    else:
        print("Thanks for playing")
        game_on = False
        break
