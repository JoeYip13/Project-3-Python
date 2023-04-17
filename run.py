"""
Modules
"""
from random import randint
import sys
import os
import intro
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
"""
Install colorama. Followed handy tutorial from Tech With Tim
https://www.youtube.com/watch?v=u51Zjlnui4Y
"""
""" ----- A game of Battleships. -----"""
# A single player game against the computer.
# Rules of the game;
# 1. Enter your username and the game will begin.
# 2. Gameboard will automatically generate 5 random ship spaces for the user
# and computer.
# 3. Both game boards will be dsplayed. User and Computer.
# 4. Enter your X and Y co-ordinates.
# 6. Game objectives is to sink the opponents ship.
# 7. Winner is first to sink all opponents ships.
# 8. 'X' marks a miss on the board. '*' Marks a hit on board.


BOARD_SIZE = 5
NUM_OF_SHIPS = 5

player_board = []
computer_board = []
player_ships = []
computer_ships = []
computer_guesses = []
player_guesses = []

player_score = 0
computer_score = 0


def create_board(board):
    for x in range(BOARD_SIZE):
        board.append([f"{Fore.CYAN}~"] * BOARD_SIZE)
    return board


def get_username():
    """
    Gets the username
    """
    username = input(f'Enter your username:{Fore.GREEN} \n')
    print(
        f'{Fore.GREEN}Welcome to Battleships Admiral '
        f'{Style.BRIGHT}{username}!\n{Fore.RESET}'
    )
    return username


username = get_username()


def determine_first_guesser():
    """
    Function to determine who gets to guess first. Heads or tails
    """
    print("To determine who gets to go first. We'll flip a coin")
    while True:
        user_guess = input("Guess heads or tails "
                           f"({Fore.RED}H{Fore.RESET}/{Fore.RED}T{Fore.RESET}"
                           "): \n").upper()
        if user_guess in ('H', 'T'):
            break
        print(f"Invalid choice. Please enter '{Fore.RED}H{Fore.RESET}' or "
              f"'{Fore.RED}T{Fore.RESET}'.")

    coin_toss = randint(0, 1)

    if user_guess == 'H' and coin_toss == 0:
        print(f"It's {Fore.GREEN}heads{Fore.RESET}! You get to guess first.")
        return "user"
    elif user_guess == 'T' and coin_toss == 1:
        print(f"It's {Fore.GREEN}tails{Fore.RESET}! You get to guess first.")
        return "user"
    else:
        print("It's", f"{Fore.RED}heads{Fore.RESET}"
              if coin_toss == 0 else f"{Fore.RED}tails{Fore.RESET}",
              "! The enemy gets to guess first")
        return "computer"


def print_board(board, player):
    """
    Prints the board with X-axis as 1-5 and Y-axis as A-E
    Hides the computer 'S'
    """
    print(f"{Fore.GREEN}{player}'s Battle Fleet")
    print(f'{Fore.RED}    1 2 3 4 5')
    print('---------------')
    for i, row in enumerate(board):
        if board == player_board:
            print(
                f"{Fore.RED}{chr(ord('A')+i)}{Fore.RESET}"
                f" | {' '.join(row)} {Fore.WHITE}|"
            )
        else:
            hidden_row = [f'{Fore.CYAN}~' if cell == (f'{Fore.GREEN}S')
                          else cell for cell in row]
            print(
                f"{Fore.RED}{chr(ord('A')+i)}{Fore.RESET}"
                f" | {' '.join(hidden_row)} {Fore.WHITE}|"
            )
    print('---------------')
    return board


def create_ship(board, ships):
    """
    Generate random ship locations and marks the board with 'S'
    for ships
    """
    for ship in range(NUM_OF_SHIPS):
        ship_x = randint(0, len(board)-1)
        ship_y = randint(0, len(board)-1)
        while board[ship_x][ship_y] == 'S':
            ship_x = randint(0, len(board)-1)
            ship_y = randint(0, len(board)-1)
        board[ship_x][ship_y] = (f'{Fore.GREEN}S')
        ships.append((ship_x, ship_y))
        print(computer_ships)
    return ships


def get_coordinates():
    """
    Gets X and Y co-ordinate inputs and validates input to only
    take the co-ordinates within the board size
    """
    try:
        while True:
            x = input(f'{Fore.RESET}Enter X co-ordinate ({Fore.RED}A-E'
                      f'{Fore.RESET}):{Fore.RED}\n')
            if not x:
                raise ValueError(f'{Fore.RED}No input entered. '
                                 'Please try again.')
            if x.upper() not in 'ABCDE':
                raise ValueError(f'{Fore.RED}Please enter a valid letter '
                                 f'between {Style.BRIGHT}(A-E){Fore.RESET}')
                continue

            y = input(f'{Fore.RESET}Enter Y co-ordinate'
                      f'({Fore.RED}1-5{Fore.RESET}):'
                      f'{Fore.RED} \n')
            if not y:
                raise ValueError(f'{Fore.RED}No input entered.'
                                 ' Please try again.')
            if y not in '12345':
                raise ValueError(f'Please enter a valid number between'
                      f'{Style.BRIGHT}(1-5){Fore.RESET}')
                continue

            x = ord(x.upper()) - 65  # convert letter to a num between 0-4
            y = int(y) - 1  # subtracting 1 to get a number between 0-4
            return x, y

    except ValueError as err:
        print(err)
        return get_coordinates()


def valid_coordinates(x, y, board, ships):
    """
    Validates co-ordinates from player and computer inputs.
    If input hits a ship location prints '*' for hit or 'X' for miss.
    Prints updated board and message where the X and Y coordinates
    have been shot at and if its a hit or miss
    """
    if (x, y) in ships:
        board[x][y] = (f'{Fore.RED}*')
    else:
        board[x][y] = (f'{Fore.MAGENTA}X')
    if board == player_board:
        player = "Enemy"
        opponent = username
        print_board(board, opponent)
    else:
        player = username
        opponent = "Enemy"
        print_board(board, opponent)
    print(f"{player} shot at {opponent}'s fleet at "
          f"({Fore.RED}{chr(x+65)}{Fore.RESET},{Fore.RED}{y+1}{Fore.RESET})")
    if (x, y) in ships:
        result = f'{Fore.RED}HIT'
    else:
        result = f'{Fore.MAGENTA}MISS'
    print(f"is a {result}{Fore.RESET}!\n")


def count_hit_ship(board):
    """
    Counts how many ships are hit on the board and increments the count by 1
    """
    count = 0
    for x in board:
        for y in x:
            if y == (f'{Fore.RED}*'):
                count += 1
    return count


def computer_guess(board):
    """
    Generate random computer choice and loops to check if
    X and Y co-ordinates on the board are not in the
    computer_guesses list, appends X and Y. Finally prints
    'X' on the current chosen spot on the board.
    """
    while True:
        row = randint(0, len(board)-1)
        col = randint(0, len(board)-1)
        if (row, col) not in computer_guesses:
            computer_guesses.append((row, col))
            board[row][col] = (f'{Fore.MAGENTA}X')
            break
    return (row, col)


def already_guessed(x, y, guesses):
    """
    checks if the coordinates X and Y has already been guessed before in
    the guesses list. If the coordinate has already been guessed, prompt
    the user to choose another coordinate.
    """
    if (x, y) in guesses:
        print(f"{Fore.RED}You've already guessed this coordinate."
              "Enter again.")
        return False
    else:
        guesses.append((x, y))
        return True


def calculate_score():
    """
    Calculates the score of the player and the computer
    """
    global player_score
    global computer_score
    player_score = count_hit_ship(computer_board)
    computer_score = count_hit_ship(player_board)
    print(
        f"{Fore.YELLOW}Score: {Fore.GREEN}{username}{Fore.RESET}: "
        f"{Fore.RED}{player_score}{Fore.RESET} | "
        f"{Fore.RED}Enemy{Fore.RESET}: {Fore.RED}{computer_score}\n")


def calculate_winner():
    """
    Calculates the winner based on the current scores.
    """
    if player_score == NUM_OF_SHIPS:
        print(f"{Fore.GREEN}{username} wins!{Fore.RESET}"
              " Congratulations!\n")
        play_again()
    elif computer_score == NUM_OF_SHIPS:
        print(f"{Fore.RED}{username} lost!{Fore.RESET} Game over!\n")
        play_again()
    else:
        return True


def run_game():
    """
    Main game function.
    """
    num_turns = 0

    guesser_first = determine_first_guesser()

    create_board(player_board)
    create_board(computer_board)
    create_ship(player_board, player_ships)
    create_ship(computer_board, computer_ships)

    if guesser_first == "user":
        print_board(computer_board, "Enemy")
        print_board(player_board, username)
        while True:
            guess_x, guess_y = get_coordinates()
            while not already_guessed(guess_x, guess_y, player_guesses):
                guess_x, guess_y = get_coordinates()
            valid_coordinates(guess_x, guess_y, computer_board,
                              computer_ships)
            c_guess_x, c_guess_y = computer_guess(player_board)
            valid_coordinates(c_guess_x, c_guess_y, player_board,
                              player_ships)
            num_turns += 1
            calculate_score()
            print(f"Number of turns: {num_turns}")
            if not calculate_winner():
                play_again()

    else:
        print_board(player_board, username)
        print_board(computer_board, "Enemy")
        c_guess_x, c_guess_y = computer_guess(player_board)
        valid_coordinates(c_guess_x, c_guess_y, player_board,
                          player_ships)
        while True:
            guess_x, guess_y = get_coordinates()
            while not already_guessed(guess_x, guess_y, player_guesses):
                guess_x, guess_y = get_coordinates()
            valid_coordinates(guess_x, guess_y, computer_board,
                              computer_ships)
            c_guess_x, c_guess_y = computer_guess(player_board)
            valid_coordinates(c_guess_x, c_guess_y, player_board,
                              player_ships)
            num_turns += 1
            calculate_score()
            print(f"Number of turns: {num_turns}\n")
            if not calculate_winner():
                play_again()


def play_again():
    """
    Play again function will ask the player if they want to play again
    after the game has ended or exit
    """
    print(f"{Fore.RESET}Would you like to play again?\n")
    answer = input(f"Enter {Fore.GREEN}Y{Fore.RESET} or {Fore.GREEN}N\n"
                   ).upper()
    while True:
        if answer == "Y":
            print(answer)
            clear_display()
            player_board.clear()
            computer_board.clear()
            player_ships.clear()
            computer_ships.clear()
            player_guesses.clear()
            computer_guesses.clear()
            run_game()
        elif answer == "N":
            clear_display()
            print(f"{Fore.BLUE}{Style.BRIGHT}Goodbye {username}!\n")
            sys.exit()
        else:
            print(f"Please enter {Fore.GREEN}Y{Fore.RESET} or {Fore.GREEN}N\n")
            answer = input("Enter Y or N\n").upper()


def clear_display():
    """
    Function that clears the terminal display
    Guidance from:
    https://www.codingninjas.com/codestudio/library/how-to-clear-a-screen-in-python
    """
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:
        _ = os.system('clear')  # For macOS and Linux


run_game()
