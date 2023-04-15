"""
Install colorama. Followed handy tutorial from Tech With Tim
https://www.youtube.com/watch?v=u51Zjlnui4Y
"""
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


class Intro():
    """
    Introduction to the game.
    """
    def __init__(self):
        self.welcome_screen()

    def welcome_screen(self):
        """
        Display title of game, offer the player to view
        the game rules and ask if they wish to begin the 
        game
        Title taken from: https://ascii.co.uk/art/battleship
        """
        print(
            f"""{Fore.GREEN}
             _           _   _   _           _     _       
            | |         | | | | | |         | |   (_)      
            | |__   __ _| |_| |_| | ___  ___| |__  _ _ __   ___
            | '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \ / __|
            | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |\__ \ 
            |_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ |___/
                                                    | |    
                                                    |_|
            """
        )
        print(f"{Fore.GREEN}Welcome to the game Battleships!\n")
        option_menu = True
        while option_menu:
            options = input(f"Enter {Fore.GREEN}'P'{Fore.RESET} to play,"
                            f"      {Fore.GREEN}'I'{Fore.RESET} for instructions\n").upper()
            if options == "P":
                option_menu = False
                print(f"{Fore.GREEN}Starting game...")
            elif options == "I":
                option_menu = False
                self.game_instructions()
            else:
                print(f"{Fore.RED}Your input was not valid.")

    
    def game_instructions(self):
        """
        Function that explains the instructions of the game
        """
        print(
            "Your ships and Enemy ships are automatically generated and placed on the board\n"
            f"Five'{Fore.GREEN}S{Fore.RESET}'ships in total to be found\n"
            f"Enter your X coordinates ({Fore.RED}A-E{Fore.RESET}) and press 'Enter' key\n"
            f"Enter your Y coordinates ({Fore.RED}1-5{Fore.RESET}) and press 'Enter key\n"
            f"'{Fore.MAGENTA}X{Fore.RESET}' marks a miss, '{Fore.RED}*{Fore.RESET}' marks a hit\n"
            "First person to sink all opponent ships wins the game!\n"
            "Enter your username and the game will begin. Good Luck!")


Intro()