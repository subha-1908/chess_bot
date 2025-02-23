"""
All functions like static_evaluation_function, minimax that are used by the chess bot are contained in this file.
"""

import chess

# pieceValues to define each piece value on the board
pieceValues = {'K': 20000, 'R': 500, 'N': 320, 'B': 330, 'Q': 900, 'P': 100, 'k': -20000, 'r': -500, 'n': -320,
               'b': -330, 'q': -900, 'p': -100}

# lookup table for incrementing or decrementing the value of each type of the piece based on its position on the board.
whitePawn = [0, 0, 0, 0, 0, 0, 0, 0,
             50, 50, 50, 50, 50, 50, 50, 50,
             10, 10, 20, 30, 30, 20, 10, 10,
             5, 5, 10, 25, 25, 10, 5, 5,
             0, 0, 0, 20, 20, 0, 0, 0,
             5, -5, -10, 0, 0, -10, -5, 5,
             5, 10, 10, -20, -20, 10, 10, 5,
             0, 0, 0, 0, 0, 0, 0, 0]

blackPawn = [0, 0, 0, 0, 0, 0, 0, 0,
             -5, -10, -10, 20, 20, -10, -10, -5,
             -5, 5, 10, 0, 0, 10, 5, -5,
             0, 0, 0, -20, -20, 0, 0, 0,
             -5, -5, -10, -25, -25, -10, -5, -5,
             -10, -10, -20, -30, -30, -20, -10, -10,
             -50, -50, -50, -50, -50, -50, -50, -50,
             0, 0, 0, 0, 0, 0, 0, 0]

whiteKnight = [-50, -40, -30, -30, -30, -30, -40, -50,
               -40, -20, 0, 0, 0, 0, -20, -40,
               -30, 0, 10, 15, 15, 10, 0, -30,
               -30, 5, 15, 20, 20, 15, 5, -30,
               -30, 0, 15, 20, 20, 15, 0, -30,
               -30, 5, 10, 15, 15, 10, 5, -30,
               -40, -20, 0, 5, 5, 0, -20, -40,
               -50, -40, -30, -30, -30, -30, -40, -50]

blackKnight = [50, 40, 30, 30, 30, 30, 40, 50,
               40, 20, 0, -5, -5, 0, 20, 40,
               30, -5, -10, -15, -15, -10, -5, 30,
               30, 0, -15, -20, -20, -15, 0, 30,
               30, -5, -15, -20, -20, -15, -5, 30,
               30, 0, -10, -15, -15, -10, 0, 30,
               40, 20, 0, 0, 0, 0, 20, 40,
               50, 40, 30, 30, 30, 30, 40, -50]

whiteBishop = [-20, -10, -10, -10, -10, -10, -10, -20,
               -10, 0, 0, 0, 0, 0, 0, -10,
               -10, 0, 5, 10, 10, 5, 0, -10,
               -10, 5, 5, 10, 10, 5, 5, -10,
               -10, 0, 10, 10, 10, 10, 0, -10,
               -10, 10, 10, 10, 10, 10, 10, -10,
               -10, 5, 0, 0, 0, 0, 5, -10,
               -20, -10, -10, -10, -10, -10, -10, -20]

blackBishop = [20, 10, 10, 10, 10, 10, 10, 20,
               10, -5, 0, 0, 0, 0, -5, 10,
               10, -10, -10, -10, -10, -10, -10, 10,
               10, 0, -10, -10, -10, -10, 0, 10,
               10, -5, -5, -10, -10, -5, -5, 10,
               10, 0, -5, -10, -10, -5, 0, 10,
               10, 0, 0, 0, 0, 0, 0, 10,
               20, 10, 10, 10, 10, 10, 10, -20]

whiteRook = [0, 0, 0, 0, 0, 0, 0, 0,
             5, 10, 10, 10, 10, 10, 10, 5,
             -5, 0, 0, 0, 0, 0, 0, -5,
             -5, 0, 0, 0, 0, 0, 0, -5,
             -5, 0, 0, 0, 0, 0, 0, -5,
             -5, 0, 0, 0, 0, 0, 0, -5,
             -5, 0, 0, 0, 0, 0, 0, -5,
             0, 0, 0, 5, 5, 0, 0, 0]

blackRook = [0, 0, 0, -5, -5, 0, 0, 0,
             5, 0, 0, 0, 0, 0, 0, 5,
             5, 0, 0, 0, 0, 0, 0, 5,
             5, 0, 0, 0, 0, 0, 0, 5,
             5, 0, 0, 0, 0, 0, 0, 5,
             5, 0, 0, 0, 0, 0, 0, 5,
             -5, -10, -10, -10, -10, -10, -10, -5,
             0, 0, 0, 0, 0, 0, 0, 0]

whiteQueen = [-20, -10, -10, -5, -5, -10, -10, -20,
              -10, 0, 0, 0, 0, 0, 0, -10,
              -10, 0, 5, 5, 5, 5, 0, -10,
              -5, 0, 5, 5, 5, 5, 0, -5,
              0, 0, 5, 5, 5, 5, 0, -5,
              -10, 5, 5, 5, 5, 5, 0, -10,
              -10, 0, 5, 0, 0, 0, 0, -10,
              -20, -10, -10, -5, -5, -10, -10, -20]

blackQueen = [20, 10, 10, 5, 5, 10, 10, 20,
              10, 0, 0, 0, 0, -5, 0, 10,
              10, 0, -5, -5, -5, -5, -5, 10,
              5, 0, -5, -5, -5, -5, 0, 0,
              5, 0, -5, -5, -5, -5, 0, 5,
              10, 0, -5, -5, -5, -5, 0, 10,
              10, 0, 0, 0, 0, 0, 0, 10,
              20, 10, 10, 5, 5, 10, 10, -20]

whiteKingMiddleGame = [-30, -40, -40, -50, -50, -40, -40, -30,
                       -30, -40, -40, -50, -50, -40, -40, -30,
                       -30, -40, -40, -50, -50, -40, -40, -30,
                       -30, -40, -40, -50, -50, -40, -40, -30,
                       -20, -30, -30, -40, -40, -30, -30, -20,
                       -10, -20, -20, -20, -20, -20, -20, -10,
                       20, 20, 0, 0, 0, 0, 20, 20,
                       20, 30, 10, 0, 0, 10, 30, 20]

blackKingMiddleGame = [-20, -30, -10, 0, 0, -10, -30, -20,
                       -20, -20, 0, 0, 0, 0, -20, -20,
                       10, 20, 20, 20, 20, 20, 20, 10,
                       20, 30, 30, 40, 40, 30, 30, 20,
                       30, 40, 40, 50, 50, 40, 40, 30,
                       30, 40, 40, 50, 50, 40, 40, 30,
                       30, 40, 40, 50, 50, 40, 40, 30,
                       30, 40, 40, 50, 50, 40, 40, -30]

whiteKingEndGame = [-50, -40, -30, -20, -20, -30, -40, -50,
                    -30, -20, -10, 0, 0, -10, -20, -30,
                    -30, -10, 20, 30, 30, 20, -10, -30,
                    -30, -10, 30, 40, 40, 30, -10, -30,
                    -30, -10, 30, 40, 40, 30, -10, -30,
                    -30, -10, 20, 30, 30, 20, -10, -30,
                    -30, -30, 0, 0, 0, 0, -30, -30,
                    -50, -30, -30, -30, -30, -30, -30, -50]

blackKingEndGame = [50, 30, 30, 30, 30, 30, 30, 50,
                    30, 30, 0, 0, 0, 0, 30, 30,
                    30, 10, -20, -30, -30, -20, 10, 30,
                    30, 10, -30, -40, -40, -30, 10, 30,
                    30, 10, -30, -40, -40, -30, 10, 30,
                    30, 10, -20, -30, -30, -20, 10, 30,
                    30, 20, 10, 0, 0, 10, 20, 30,
                    50, 40, 30, 20, 20, 30, 40, -50]

squareValues = {'K': whiteKingMiddleGame, 'R': whiteRook, 'N': whiteKnight, 'B': whiteBishop, 'Q': whiteQueen,
                'P': whitePawn, 'k': blackKingMiddleGame, 'r': blackRook, 'n': blackKnight,
                'b': blackBishop, 'q': blackQueen, 'p': blackPawn}


def static_evaluation_function(board: chess.Board) -> int:
    """
    Evaluates the value of the current position based on the material available on the board.
    :param board: defines the current state of the board
    :return: returns the integer value that represents the static value of the current state.
    """
    result = 0
    current_square = 56
    for i in board.fen():
        if i in pieceValues:
            result = result + pieceValues[i] + squareValues[i][current_square]
            current_square = current_square + 1

        elif i == "/":
            current_square = current_square - 16

        elif i == " ":
            return result

        else:
            current_square = current_square + int(i)
    return result


def move_arranger(board: chess.Board, legal_moves):
    """
    This function returns the ordered moves based on their priority and effectiveness.
    :param board: Represents the current state of the board.
    :param legal_moves: The set of all the legal moves that are possible on the current state of the board.
    :return: Returns the legal moves that are taken as input but arranged in the order of their significance.
    """
    captures = []
    checks = []
    promotions = []
    quiet_moves = []
    for i in legal_moves:
        if board.is_capture(i):
            captures.append(i)

        elif board.gives_check(i):
            checks.append(i)

        elif i.promotion:
            promotions.append(i)

        else:
            quiet_moves.append(i)

    captures.sort(key=lambda m: (
        pieceValues.get(board.piece_type_at(m.to_square), 0),  # Victim's value
        -pieceValues.get(board.piece_type_at(m.from_square), 0)  # Attacker's value (negative for priority)
    ), reverse=True)
    moves = captures + checks + promotions + quiet_moves
    return moves


def minimax(board: chess.Board, depth: int, maximizingPlayer: bool, alpha: int, beta: int) -> int:
    """
    checks which position would lead to the best possible position from the current state after some half moves deep.
    :param board: represents the current state of the board.
    :param depth: represents the depth of the tree i.e, the number of half moves deep search.
    :param alpha: represents alpha which is used for alpha-beta pruning.
    :param beta: represents beta which is used for alpha beta pruning.
    :param maximizingPlayer: If true then it is white to move, else it is black's turn.
    :return: returns the static value of the best state possible form the given position.
    """
    if depth == 0 or board.is_checkmate() or board.is_stalemate() or board.is_seventyfive_moves():
        return static_evaluation_function(board)

    if maximizingPlayer:
        maxEval = -40000
        moves = move_arranger(board, board.legal_moves)
        for move in moves:
            temp = board.copy()
            temp.push(move)
            eval_ = minimax(temp, depth - 1, False, alpha, beta)
            maxEval = max(maxEval, eval_)
            alpha = max(alpha, eval_)
            if beta <= alpha:
                break
        return maxEval

    else:
        minEval = 40000
        moves = move_arranger(board, board.legal_moves)
        for move in moves:
            temp = board.copy()
            temp.push(move)
            eval_ = minimax(temp, depth - 1, True, alpha, beta)
            minEval = min(beta, eval_)
            beta = min(beta, eval_)
            if beta <= alpha:
                break
        return minEval

