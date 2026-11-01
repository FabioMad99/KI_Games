
def check_winner(board):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


def minimax(board, is_maximizing):
    winner = check_winner(board)

    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if winner == "Draw":
        return 0

    if is_maximizing:
        best_score = float("-inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score


def find_best_move(board):
    best_score = float("-inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")


def main():
    board = [" "] * 9

    while True:
        print_board(board)

        # Mensch spielt
        move = int(input("Dein Zug (1-9): ")) - 1

        if move < 0 or move > 8 or board[move] != " ":
            print("Ungültiger Zug!")
            continue

        board[move] = "X"

        if check_winner(board) is not None:
            break

        # Computer spielt mit Minimax
        move = find_best_move(board)
        board[move] = "O"

        if check_winner(board) is not None:
            break

    print_board(board)

    winner = check_winner(board)

    if winner == "Draw":
        print("Unentschieden!")
    else:
        print(winner, "hat gewonnen!")


main()
