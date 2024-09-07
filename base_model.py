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

def drop_piece(board, row, col, piece):
    """Places a piece o the board"""
    board[row][col] = piece

def is_valid_location(board, col):
    """Checks if the board is valid"""
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    """Finds the next open row in the column"""
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def winning_move(board, piece):
    """Checks if a player has own"""

    #Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 1] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r -1 ][c + 1] == piece and board[r -2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

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
    """Main function for simulate"""
    board = create_board()
    game_over = False
    turn = 0

    while not game_over:
        # Random Player Turn
        col = random.randint(0, COLUMN_COUNT - 1)

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, turn + 1)

            if winning_move(board, turn + 1):
                print(f"Player {turn + 1} wins!")
                game_over = True

        turn += 1
        turn = turn % 2

    print_board(board)
    draw_board(board)

play_game()