def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {current_player}, enter column (0, 1, 2): "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid position! Choose row and column between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Choose another.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break

        if is_draw(board):
            print("It's a draw! 🤝")
            break

        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()
