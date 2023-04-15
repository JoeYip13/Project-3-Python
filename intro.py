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
            """
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
        print("Welcome to the game Battleships!\n")
        option_menu = True
        while option_menu:
            options = input("Enter 'P' to play,"
                            "      'I' for instructions\n").upper()
            if options == "P":
                option_menu = False
                print("Starting game")
            elif options == "I":
                option_menu = False
                self.game_instructions()
            else:
                print("Your input was not valid.")

    
    def game_instructions(self):
        """
        Function that explains the instructions of the game
        """
        print(
            "Your ships and Enemy ships are automatically genertated and placed on the board\n"
            "5 Ships in total to be found\n"
            "Enter your X coordinates (A-E) and press 'Enter' key\n"
            "Enter your Y coordinates (1-5) and press 'Enter key\n"
            "'X' marks a miss, '*' marks a hit\n"
            "First person to sink all ships wins the game!\n"
            "Enter your username and the game will begin. Good Luck!")


Intro()