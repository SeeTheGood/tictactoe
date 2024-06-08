Tic-Tac-Toe Game

This repository contains a Python implementation of the classic Tic-Tac-Toe game with an AI component.

Features

Initial State: Generates the starting state of the board.
Player Turn: Determines which player (X or O) has the next turn.
Possible Actions: Identifies all possible moves on the current board.
Resulting Board: Produces the new board state after a move.
Winner Determination: Checks if there is a winner.
Game Over Check: Determines if the game has ended.
Utility Function: Calculates the utility of a board state.
Minimax Algorithm: Implements the minimax algorithm to determine the optimal move.
Usage

To play the game or test the AI, run the script in a Python environment with the required dependencies installed.

Functions Overview

initial_state(): Returns the starting state of the board.
player(board): Returns the player who has the next turn on the board.
actions(board): Returns a set of all possible actions available on the board.
result(board, action): Returns the board that results from making a move.
winner(board): Returns the winner of the game, if there is one.
terminal(board): Returns True if the game is over, False otherwise.
utility(board): Returns 1 if X has won, -1 if O has won, 0 otherwise.
minimax(board): Returns the optimal action for the current player on the board.
Running the Script

To run the script, simply execute it in a Python environment: python tictactoe.py

Feel free to modify and extend the code to add more features or improve the AI!
