def evaluate_window(window, player):
    score = 0
    opp_player = 3 - player

    if window.count(player) == 4:
        score += 100
    elif window.count(player) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(player) == 2 and window.count(0) == 2:
        score += 2
    if window.count(opp_player) == 3 and window.count(0) == 1:
        score -= 4
    return score

def heuristic(game, player):
    board = game.board
    score = 0

    # Horizontal
    for row in board:
        for c in range(7 - 3):
            window = row[c:c+4]
            score += evaluate_window(window, player)

    # Vertical
    for c in range(7):
        col_array = [board[r][c] for r in range(6)]
        for r in range(6 - 3):
            window = col_array[r:r+4]
            score += evaluate_window(window, player)

    # Positive Diagonal
    for r in range(6 - 3):
        for c in range(7 - 3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, player)

    # Negative Diagonal
    for r in range(3, 6):
        for c in range(7 - 3):
            window = [board[r-i][c+i] for i in range(4)]
            score += evaluate_window(window, player)

    return score
