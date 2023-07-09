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
