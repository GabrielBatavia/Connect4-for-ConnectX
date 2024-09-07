import numpy as np
import random
import matplotlib.pyplot as plt

# The board size
ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    """Create a 6*7 board"""
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def draw_board(board):
    """Draws the board using matplotlib"""
    plt.imshow(np.flip(board, 0), cmap='coolwarm', interpolation='nearest')
    plt.title('Connect 4 Board')
    plt.xticks(range(COLUMN_COUNT))
    plt.yticks(range(ROW_COUNT))
    plt.show()

def print_board(board):
    """Flips the board so the botton row is at the bottom when visualizing"""
    print(np.flip(board, 0))

def play_game():
    board = create_board()

    print_board(board)
    draw_board(board)

play_game()