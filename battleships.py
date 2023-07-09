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
