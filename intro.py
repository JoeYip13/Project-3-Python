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
                   

Intro()