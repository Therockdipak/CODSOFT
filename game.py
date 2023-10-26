import random

# Constants for the players
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

# Define the Tic-Tac-Toe board
board = [EMPTY] * 9

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")

# Function to check if the game has ended
def game_over(board):
    # Check for a win
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != EMPTY:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != EMPTY:
            return True
    if board[0] == board[4] == board[8] != EMPTY or board[2] == board[4] == board[6] != EMPTY:
        return True

    # Check for a tie
    if EMPTY not in board:
        return True

    return False

# Function to evaluate the board
def evaluate(board):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == AI:
            return 10
        elif board[i] == board[i+1] == board[i+2] == HUMAN:
            return -10
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == AI:
            return 10
        elif board[i] == board[i+3] == board[i+6] == HUMAN:
            return -10
    if board[0] == board[4] == board[8] == AI or board[2] == board[4] == board[6] == AI:
        return 10
    elif board[0] == board[4] == board[8] == HUMAN or board[2] == board[4] == board[6] == HUMAN:
        return -10
    return 0

# Minimax with Alpha-Beta Pruning
def minimax(board, depth, is_max, alpha, beta):
    if game_over(board):
        return evaluate(board)

    if is_max:
        max_eval = -float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = EMPTY
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Function to find the best move using minimax
def find_best_move(board):
    best_eval = -float('inf')
    best_move = -1
    alpha = -float('inf')
    beta = float('inf')
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            eval = minimax(board, 0, False, alpha, beta)
            board[i] = EMPTY
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Main game loop
while True:
    print_board(board)
    move = -1

    if EMPTY in board:
        while move < 0 or move > 8 or board[move] != EMPTY:
            try:
                move = int(input("Enter your move (0-8): "))
            except ValueError:
                pass
    else:
        print("It's a tie!")
        break

    board[move] = HUMAN

    if game_over(board):
        print_board(board)
        print("You win!")
        break

    best_move = find_best_move(board)
    board[best_move] = AI

    if game_over(board):
        print_board(board)
        print("AI wins!")
        break
