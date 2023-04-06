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
from random import randint


def get_username():
    """
    Gets the username
    """
    username = input('Enter your username: ')
    print(f'Welcome to Battleships Admiral {username}!')

    return username


BOARD_SIZE = 5
NUM_OF_SHIPS = 5

player_board = []
computer_board = []
player_ships = []
computer_ships = []
computer_guesses = []

username = get_username()
for x in range(BOARD_SIZE):
    player_board.append(["O"] * BOARD_SIZE)
    computer_board.append(['O'] * BOARD_SIZE)


def print_board(board, player):
    """
    Prints the board
    """
    print(f"{player}'s Battle Fleet")
    print('----------')
    for row in board:
        print(" ".join(row))
    print('----------')

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
        board[ship_x][ship_y] = 'S'
        ships.append((ship_x, ship_y))
        print(ships)
    return ships


def get_coordinates():
    """
    Gets X and Y co-ordinate inputs and validates input to only
    take the co-ordinates within the board size
    """
    x = input('Enter X co-ordinate (1-5): ')
    while x not in '12345':
        print('Please enter a valid number')
        x = input('Enter X co-ordinate (1-5): ')
    y = input('Enter Y co-ordinate (1-5): ')
    while y not in '12345':
        print('Please enter a valid number')
        y = input('Enter Y co-ordinate (1-5): ')

    return int(x)-1, int(y)-1


def valid_coordinates(x, y, board, ships):
    """
    Validates co-ordinates from the get_coordinates function to see if
    player has hit or miss
    """
    if (x, y) in ships:
        print(f'Direct HIT! Admiral {username} You sunk a enemy ship!')
        board[x][y] = '*'
        count_hit_ship(computer_board)
        computer_choice(player_board)
        print_board(player_board, username)
        print_board(computer_board, "Enemy")
    else:
        print(f'MISS. No hit Admiral {username}')
        board[x][y] = 'X'
        computer_choice(player_board)
        print_board(player_board, username)
        print_board(computer_board, "Enemy")


def count_hit_ship(board):
    """
    Counts how many ships are hit on the board and increments the count by 1
    """
    count = 0
    for x in board:
        for y in x:
            if y == '*':
                count += 1
                print(f"Total ships sunk: {count}")
    return count


def computer_choice(board):
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
            print(computer_guesses)
            board[row][col] = 'X'
        break
    return (row, col)


create_ship(player_board, player_ships)
create_ship(computer_board, computer_ships)
print_board(player_board, username)
print_board(computer_board, "Enemy")

guess_x, guess_y = get_coordinates()
valid_coordinates(guess_x, guess_y, computer_board, computer_ships)
