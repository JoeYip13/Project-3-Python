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


BOARD_SIZE = 5
NUM_OF_SHIPS = 2

player_board = []
computer_board = []
player_ships = []
computer_ships = []
computer_guesses = []
player_guesses = []

player_score = 0
computer_score = 0

for x in range(BOARD_SIZE):
    player_board.append(["~"] * BOARD_SIZE)
    computer_board.append(['~'] * BOARD_SIZE)


def get_username():
    """
    Gets the username
    """
    username = input('Enter your username: ')
    print(f'Welcome to Battleships Admiral {username}!')

    return username


username = get_username()


def print_board(board, player):
    """
    Prints the board with X-axis as 1-5 and Y-axis as A-E
    """
    print(f"{player}'s Battle Fleet")
    print('    1 2 3 4 5')
    print('---------------')
    for i, row in enumerate(board):
        print(f"{chr(ord('A')+i)} | {' '.join(row)} |")
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
        board[ship_x][ship_y] = 'S'
        ships.append((ship_x, ship_y))
    return ships


def get_coordinates():
    """
    Gets X and Y co-ordinate inputs and validates input to only
    take the co-ordinates within the board size
    """
    try:
        x = input('Enter X co-ordinate (A-E): ')
        if not x:
            raise ValueError('No input entered. Please try again.')
        if x.upper() not in 'ABCDE':
            raise ValueError('Please enter a valid letter between (A-E)')

        while True:
            y = input('Enter Y co-ordinate (1-5): ')
            if not y:
                raise ValueError('No input entered. Please try again.')
            if y not in '12345':
                print('Please enter a valid number between (1-5)')
            else:
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
        board[x][y] = '*'
    else:
        board[x][y] = 'X'
    if board == player_board:
        player = "Enemy"
        opponent = username
        print_board(board, opponent)
    else:
        player = username
        opponent = "Enemy"
        print_board(board, opponent)
    print(f"{player} shot at {opponent}'s fleet at ({chr(x+65)},{y+1})")
    print(f"is a {'HIT' if (x,y) in ships else 'MISS'}!\n")


def count_hit_ship(board):
    """
    Counts how many ships are hit on the board and increments the count by 1
    """
    count = 0
    for x in board:
        for y in x:
            if y == '*':
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
            board[row][col] = 'X'
            break
    return (row, col)


def already_guessed(x, y, guesses):
    """
    checks if the coordinates X and Y has already been guessed before in
    the guesses list. If the coordinate has already been guessed, prompt
    the user to choose another coordinate.
    """
    if (x, y) in guesses:
        print("You've already guessed this coordinate. Enter again.")
        return False
    else:
        guesses.append((x, y))
        print(guesses)
        return True


def calculate_score():
    """
    Calculates the score of the player and the computer
    """
    global player_score
    global computer_score
    player_score = count_hit_ship(computer_board)
    computer_score = count_hit_ship(player_board)
    print(f"Score: {username}: {player_score}, Enemy: {computer_score}\n")


def run_game():
    """
    Main game function.
    """
    create_ship(player_board, player_ships)
    create_ship(computer_board, computer_ships)
    print_board(player_board, username)
    print_board(computer_board, "Enemy")

    while True:
        guess_x, guess_y = get_coordinates()
        while not already_guessed(guess_x, guess_y, player_guesses):
            guess_x, guess_y = get_coordinates()
        c_guess_x, c_guess_y = computer_guess(player_board)

        valid_coordinates(c_guess_x, c_guess_y, player_board, player_ships)
        calculate_score()
        if computer_score == NUM_OF_SHIPS:
            print(f"{username} lost! Game over!")
            break
        valid_coordinates(guess_x, guess_y, computer_board, computer_ships)
        calculate_score()
        if player_score == NUM_OF_SHIPS:
            print(f"{username} wins! Congratulations!")
            break

        # if count_hit_ship(computer_board) == 2:
        #     print("You sunk all the Enemy ships! You win!")
        #     return False
        # if count_hit_ship(player_board) == 5:
        #     print("Enemy has sunk all your ships. Game Over!")
        #     return False


run_game()
