def display_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def check_winner(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False
def check_draw(board):
    return " " not in board
def play_game():
    board = [" "] * 9  
    current_player = "X"
    print("Welcome to Tic-Tac-Toe!")
    display_board(board)

    while True:
        try:
            move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        if move < 0 or move > 8:
            print("Invalid move. Please choose an empty spot between 1 and 9.")
        elif board[move] != " ":
            print("Press Something between 1 to 8")
            continue

        board[move] = current_player
        display_board(board)
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"
play_game()