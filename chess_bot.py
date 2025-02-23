import chess
import all_chess_functions  # Import your custom chess functions


def print_board(board):
    print(board)
    print()


def get_human_move(board):
    """Prompt the user to enter a valid move."""
    while True:
        user_move = input("Your move (e.g., e2e4): ").strip()
        try:
            move = chess.Move.from_uci(user_move)
            if move in board.legal_moves:
                return move
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid move format. Please use standard UCI format (e.g., e2e4).")


def get_bot_move(board, depth, white):
    """Generate the bot's move using Minimax algorithm."""
    possible_states = []
    moves = list(board.legal_moves)

    for move in moves:
        temp = board.copy()
        temp.push(move)
        possible_states.append(temp)

    eval_values = [all_chess_functions.minimax(state, depth, white, -40000, 40000) for state in possible_states]

    if white:
        best_eval = max(eval_values)
    else:
        best_eval = min(eval_values)

    best_move = moves[eval_values.index(best_eval)]
    return best_move


def main():
    board = chess.Board()
    print_board(board)

    no_of_moves = 0
    white_to_move = True

    # Ask the user to choose their color
    user_is_white = input("Do you want to play as White? (y/n): ").strip().lower() == 'y'

    while not board.is_game_over():
        if (white_to_move and user_is_white) or (not white_to_move and not user_is_white):
            # Human's turn
            print("Your turn:")
            move = get_human_move(board)
        else:
            # Bot's turn
            print("Bot's turn...")
            move = get_bot_move(board, depth=4, white=white_to_move)
            print(f"Bot plays: {move.uci()}")

        board.push(move)
        print_board(board)

        # Switch turns
        white_to_move = not white_to_move
        no_of_moves += 1

    print(f"Game over in {no_of_moves} moves!")
    print(f"Result: {board.result()}")


if __name__ == "__main__":
    main()
