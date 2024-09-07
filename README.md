# Connect4-for-ConnectX

## Connect 4: Python Simulation with Random Agents

This repository contains a simple simulation of the classic **Connect 4** game implemented in Python. Two random agents take turns to play the game, and the board is visualized after each move. The game ends when one of the players connects four pieces horizontally, vertically, or diagonally.

## Features

- **6x7 Game Board**: Standard Connect 4 grid with 6 rows and 7 columns.
- **Random Agents**: Two players pick random columns to drop their pieces.
- **Win Condition Detection**: The game checks for horizontal, vertical, and diagonal connections of 4 pieces.
- **Board Visualization**: The game board is visualized using Matplotlib after each turn.

## Game Rules

- Players take turns dropping their pieces into one of the columns.
- The pieces fall to the lowest available spot in the selected column.
- The game ends when a player connects 4 pieces in a row, either horizontally, vertically, or diagonally.
- If no valid moves are left, the game ends in a draw.
