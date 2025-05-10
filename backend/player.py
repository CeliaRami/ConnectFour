class Player:
    def __init__(self, player_id):
        self.player_id = player_id

class HumanPlayer(Player):
    def get_move(self, game):
        col = int(input(f"Player {self.player_id}, enter your move (0-6): "))
        return col

class AIPlayer(Player):
    def __init__(self, player_id, depth, heuristic):
        super().__init__(player_id)
        self.depth = depth
        self.heuristic = heuristic

    def get_move(self, game):
        from minimax import minimax
        _, move = minimax(game, self.depth, True, float("-inf"), float("inf"), self.player_id, self.heuristic)
        return move
