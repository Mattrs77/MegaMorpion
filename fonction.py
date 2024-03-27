def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != None:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != None:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != None:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != None:
        return True

    return False