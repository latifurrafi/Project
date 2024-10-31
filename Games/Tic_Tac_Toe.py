# Function to display the Tic-Tac-Toe board
def display_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

# Function to check if there is a winner
def check_winner(board, player):
    # All possible winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    # Check if any winning combination is matched by the current player
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full
def check_draw(board):
    return " " not in board

# Main function for Tic-Tac-Toe game
def play_game():
    board = [" "] * 9  # Initial empty board
    current_player = "X"  # X always starts

    print("Welcome to Tic-Tac-Toe!")
    display_board(board)

    while True:
        # Get the player's move
        try:
            move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        # Check if the move is valid
        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move. Please choose an empty spot between 1 and 9.")
            continue

        # Place the player's mark on the board
        board[move] = current_player
        display_board(board)

        # Check for a winner or a draw
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
