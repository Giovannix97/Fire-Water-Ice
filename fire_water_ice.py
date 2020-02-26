import random
import logging
import game_gui
from enum import Enum

logging.basicConfig(level=logging.DEBUG)



class Elements(Enum):
    """ An enum that models the three elements of the game."""
    FIRE  = 1
    WATER = 2
    ICE   = 3



class Winner(Enum):
    """ Each value of this enum represents a different case of winner."""
    PLAYER   = 1
    COMPUTER = 2
    DRAW     = 3



def get_computer_choice():
    """ Get a random number between 1 and 3. This represents computer's choice

        Returns:
        int: A random number from 1 to 3
    """
    value = random.randint(1,3)
    logging.info("Computer random number is: {}".format(value))
    return value



def get_computer_choice_name(number):
    """ Get the random numeric value chosen by computer and return the relative element

        Parameters:
        number (int): A random int value from 1 to 3 that represents an element of the game

        Returns:
        Elements: The corresponding value in the Enum

     """
    logging.info("Computer random element is: {} ".format(Elements(number).name))
    return Elements(number).name



def get_user_choice(choice):
    """ Get user choice from the gui. This function is invoked as callback of a button.

        Parameters:
        choice (int): A number from 1 to 3 that represents user's choice
    """
    logging.info("User's choice is {}".format(choice))

    # If the user clicks an element, this means he wants to start a new game
    return start_new_game(choice)   



def start_new_game(user_choice):
    """ Start a new game.

        Parameters:
        user_choice (int): value chosen by user

        Returns:
        winner (Winner): an enum value that represent the winner 
    """
    logging.info("Started new game")
    computer_c = get_computer_choice()
    
    temp_list = []
    temp_list.append(get_winner(user_choice,computer_c).value)
    temp_list.append(Elements(computer_c).name)

    return temp_list
   


def get_winner(user_choice,computer_choice):
    """ Check the two choices and determines the winner of the match

        Parameter:
        user_choice     (int): an int value from 1 to 3 that represents user's choice
        computer_choice (int): an int value from 1 to 3 that represents computer's choice

        Returns:
        Winner : an enum value that represent the winner
    """
    
    if(user_choice == computer_choice):
        # Draw
        return Winner.DRAW
    elif((user_choice == 1 and computer_choice == 3) or (user_choice == 3 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1)):
        # User Wins
        #
        # Case 1 : Fire melts Ice
        # Case 2 : Ice freezes Water
        # Case 3 : Water extinguishes Fire
        return Winner.PLAYER
    else:
        # Computer Wins
        return Winner.COMPUTER


        


    

     

