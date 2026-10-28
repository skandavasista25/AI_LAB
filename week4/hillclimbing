import random

def heuristic(board):
    h = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                h += 1
    return h

def print_board(board):
    for r in range(4):
        print(" ".join("Q" if board[r] == c else "." for c in range(4)))
    print()

def hill_climbing():
    board = [random.randint(0, 3) for _ in range(4)]
    step = 0

    while True:
        h = heuristic(board)
        print("Step:", step, "Board:", board, "Heuristic:", h)
        print_board(board)

        if h == 0:
            print("Solution found!")
            return

        best = board[:]
        best_h = h

        for row in range(4):
            for col in range(4):
                temp = board[:]
                temp[row] = col
                score = heuristic(temp)

                if score < best_h:
                    best = temp
                    best_h = score

        if best_h >= h:
            print("Local optimum! Restarting...\n")
            return hill_climbing()

        board = best
        step += 1

hill_climbing()
