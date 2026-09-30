board = [" "] * 9
def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
def winner(p):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == p:
            return True
    return False
def minimax(maximizing):
    if winner("X"):
        return 10
    if winner("O"):
        return -10
    if " " not in board:
        return 0
    if maximizing:
        best = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)
        return best
def best_move():
    best_score = -100
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move
while True:
    print_board()
    move = int(input("Enter your move (1-9): ")) - 1
    if board[move] != " ":
        print("Invalid move!")
        continue
    board[move] = "O"
    if winner("O"):
        print_board()
        print("You win!")
        break
    if " " not in board:
        print_board()
        print("Draw!")
        break
    move = best_move()
    board[move] = "X"
    if winner("X"):
        print_board()
        print("AI wins!")
        break
    if " " not in board:
        print_board()
        print("Draw!")
        break
