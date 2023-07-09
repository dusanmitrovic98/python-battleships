import random

# Create the game board
board_size = 10
board = []
for x in range(board_size):
    board.append([" "] * board_size)

# Create the player and computer boards
player_board = []
computer_board = []
for x in range(board_size):
    player_board.append([" "] * board_size)
    computer_board.append([" "] * board_size)

# Function to print the game board
def print_board(board):
    symbols = {" ": " ", "S": " ", "X": "X", "M": "M"}
    line = " " + "----" * board_size
    print("  " + " ".join([str(i) for i in range(board_size)]))
    print(line)
    for i, row in enumerate(board):
        print(str(i) + " | " + " | ".join([symbols[ch] for ch in row]) + " |")
        print(line)

# Function to place ships on the board
def place_ships(board, num_ships):
    ships_placed = 0
    while ships_placed < num_ships:
        ship_row = random.randint(0, board_size - 1)
        ship_col = random.randint(0, board_size - 1)
        if board[ship_row][ship_col] == " ":
            board[ship_row][ship_col] = "S"
            ships_placed += 1

# Function to play the game
def play_game():
    print("Let's play Battleship!")
    print("Player's Board:")
    print_board(player_board)
    print("Computer's Board:")
    print_board(board)
    player_ships = 5  # Number of player's ships
    computer_ships = 5  # Number of computer's ships
    place_ships(player_board, player_ships)  # Place player's ships

    # Place computer's ships
    place_ships(computer_board, computer_ships)

    turns = 10  # Number of turns allowed

    for turn in range(turns):
        print("Turn", turn + 1)
        guess_row = int(input("Guess Row (0-9): "))
        guess_col = int(input("Guess Col (0-9): "))

        if (
            guess_row < 0
            or guess_row >= board_size
            or guess_col < 0
            or guess_col >= board_size
        ):
            print("Oops, that's not even in the ocean.")
        elif player_board[guess_row][guess_col] == "X" or player_board[guess_row][guess_col] == "M":
            print("You guessed that one already.")
        elif player_board[guess_row][guess_col] == "S":
            print("Congratulations! You sunk one of your opponent's battleships!")
            player_board[guess_row][guess_col] = "X"
            computer_ships -= 1
        else:
            print("You missed the battleship!")
            player_board[guess_row][guess_col] = "M"

        # Computer's turn
        comp_guess_row = random.randint(0, board_size - 1)
        comp_guess_col = random.randint(0, board_size - 1)

        if board[comp_guess_row][comp_guess_col] == "X" or board[comp_guess_row][comp_guess_col] == "M":
            print("Computer guessed that one already.")
        elif board[comp_guess_row][comp_guess_col] == "S":
            print("Oh no! The computer sunk one of your battleships!")
            board[comp_guess_row][comp_guess_col] = "X"
            player_ships -= 1
        else:
            print("The computer missed your battleship!")
            board[comp_guess_row][comp_guess_col] = "M"

        # Print the updated boards
        print("Player's Board:")
