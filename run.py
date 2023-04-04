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


def username():
    """
    Gets the username
    """
    user = input('Enter your username: ')
    print(f'Welcome to Battleships Admiral {user}!')

    return user


BOARD_SIZE = 5
board = []
for x in range(BOARD_SIZE):
    board.append(["O"] * BOARD_SIZE)


def print_board(board):
    """
    Prints the board
    """
    print('----------')
    for row in board:
        print(" ".join(row))
    print('----------')

    return board


print_board(board)