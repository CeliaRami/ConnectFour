import copy

def minimax(game, depth, maximizing, alpha, beta, player_id, heuristic):
    winner = game.check_winner()
    if depth == 0 or winner != 0 or game.is_full():
        return heuristic(game, player_id), None

    valid_moves = game.get_valid_moves()
    best_move = None

    if maximizing:
        max_eval = float("-inf")
        for move in valid_moves:
            new_game = copy.deepcopy(game)
            new_game.make_move(move)
            new_game.switch_player()
            eval, _ = minimax(new_game, depth - 1, False, alpha, beta, player_id, heuristic)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float("inf")
        for move in valid_moves:
            new_game = copy.deepcopy(game)
            new_game.make_move(move)
            new_game.switch_player()
            eval, _ = minimax(new_game, depth - 1, True, alpha, beta, player_id, heuristic)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move
