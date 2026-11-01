
import math

board = [" "] * 9


# winner check
def check_winner(board):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


# Minimax Alg
def minimax(board, is_maximizing, counter):
    counter[0] += 1

    winner = check_winner(board)

    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if winner == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False, counter)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True, counter)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


# Minimax mit AlphaBeta Pruning
def minimax_alpha_beta(board, is_maximizing, alpha, beta, counter):
    counter[0] += 1

    winner = check_winner(board)

    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if winner == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax_alpha_beta(
                    board, False, alpha, beta, counter
                )
                board[i] = " "

                best_score = max(best_score, score)
                alpha = max(alpha, best_score)

                if alpha >= beta:
                    break

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax_alpha_beta(
                    board, True, alpha, beta, counter
                )
                board[i] = " "

                best_score = min(best_score, score)
                beta = min(beta, best_score)

                if alpha >= beta:
                    break

        return best_score


# Besten Zug für den Computer finden
def find_best_move(board):
    best_score = -math.inf
    best_move = None

    counter = [0]

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax_alpha_beta(
                board, False, -math.inf, math.inf, counter
            )

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


# feld anzeigen
def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(
            board[j] if board[j] != " " else str(j + 1)
            for j in range(i, i + 3)
        ))
        if i < 6:
            print("---+---+---")
    print()


def compare_algorithms():
    counter_minimax = [0]
    counter_alpha_beta = [0]

    minimax(board, True, counter_minimax)

    minimax_alpha_beta(
        board, True, -math.inf, math.inf, counter_alpha_beta
    )

    print("Knotenvergleich:")
    print("Minimax:", counter_minimax[0])
    print("Alpha-Beta:", counter_alpha_beta[0])


def play_game():
    print("\nTic Tac Toe")
    print("Du bist X, der Computer ist O.")

    while True:
        print_board(board)

        # player move
        try:
            move = int(input("Dein Zug (1-9): ")) - 1
        except ValueError:
            print("Bitte eine Zahl eingeben.")
            continue

        if move < 0 or move > 8 or board[move] != " ":
            print("Ungültiger Zug!")
            continue

        board[move] = "X"

        winner = check_winner(board)

        if winner is not None:
            break

        # KI move
        computer_move = find_best_move(board)
        board[computer_move] = "O"

        winner = check_winner(board)

        if winner is not None:
            break

    print_board(board)

    if winner == "Draw":
        print("Unentschieden!")
    else:
        print(winner, "hat gewonnen!")

if __name__ == "__main__":
    compare_algorithms()
    play_game()
