# Tic-Tac-Toe Game

# Initialize the board
board = [" " for _ in range(9)]

# Function to display the board
def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check for a win
def check_win(player):
    # Check rows, columns, and diagonals
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to check for a draw
def check_draw():
    return " " not in board

# Main game loop
current_player = "X"
while True:
    display_board()
    print(f"Player {current_player}'s turn")
    move = int(input("Enter your move (1-9): ")) - 1

    # Check if the move is valid
    if 0 <= move < 9 and board[move] == " ":
        board[move] = current_player
    else:
        print("Invalid move. Try again.")
        continue

    # Check for a win or draw
    if check_win(current_player):
        display_board()
        print(f"Player {current_player} wins!")
        break
    elif check_draw():
        display_board()
        print("It's a draw!")
        break

    # Switch players
    current_player = "O" if current_player == "X" else "X"
