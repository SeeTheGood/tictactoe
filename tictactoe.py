import math
import random
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = sum(row.count(X) for row in board)
    count_O = sum(row.count(O) for row in board)
    if count_X > count_O:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")

    player_turn = player(board)
    new_board = deepcopy(board)
    new_board[action[0]][action[1]] = player_turn
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if all(cell == X for cell in row):
            return X
        elif all(cell == O for cell in row):
            return O

    # Check columns
    for j in range(3):
        if all(board[i][j] == X for i in range(3)):
            return X
        elif all(board[i][j] == O for i in range(3)):
            return O

    # Check diagonals
    if all(board[i][i] == X for i in range(3)) or all(board[i][2-i] == X for i in range(3)):
        return X
    elif all(board[i][i] == O for i in range(3)) or all(board[i][2-i] == O for i in range(3)):
        return O

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell is not None for row in board for cell in row)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        if terminal(board):
            return utility(board), None
        v = float("-inf")
        best_action = None
        for action in actions(board):
            min_val, _ = min_value(result(board, action))
            if min_val > v:
                v = min_val
                best_action = action
        return v, best_action

    def min_value(board):
        if terminal(board):
            return utility(board), None
        v = float("inf")
        best_action = None
        for action in actions(board):
            max_val, _ = max_value(result(board, action))
            if max_val < v:
                v = max_val
                best_action = action
        return v, best_action

    if terminal(board):
        return None

    if player(board) == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]
