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


def create_ship(board):
    """
    Generate random ship locations and marks the board with 'S'
    for ships
    """
    for i in range(NUM_OF_SHIPS):
        ship_x = randint(0, len(board)-1)
        ship_y = randint(0, len(board)-1)
        while board[ship_x][ship_y] == 'S':
            ship_x = randint(0, len(board)-1)
            ship_y = randint(0, len(board)-1)
        board[ship_x][ship_y] = 'S'
    return (ship_x, ship_y)


def get_coordinates():
    """
    Gets X and Y co-ordinate inputs
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


ship_x, ship_y = create_ship(player_board)
ship_x, ship_y = create_ship(computer_board)
print_board(player_board, username)
print_board(computer_board, "Enemy")

get_coordinates()
