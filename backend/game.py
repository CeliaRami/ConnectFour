ROWS, COLS = 6, 7

class ConnectFour:
    def __init__(self):
        self.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.current_player = 1

    def make_move(self, col):
        for row in reversed(range(ROWS)):
            if self.board[row][col] == 0:
                self.board[row][col] = self.current_player
                return True
        return False

    def get_valid_moves(self):
        return [c for c in range(COLS) if self.board[0][c] == 0]

    def switch_player(self):
        self.current_player = 3 - self.current_player

    def is_full(self):
        return all(self.board[0][c] != 0 for c in range(COLS))

    def check_winner(self):
        def check_line(a, b, c, d):
            return a == b == c == d != 0

        for r in range(ROWS):
            for c in range(COLS - 3):
                if check_line(*[self.board[r][c+i] for i in range(4)]):
                    return self.board[r][c]

        for r in range(ROWS - 3):
            for c in range(COLS):
                if check_line(*[self.board[r+i][c] for i in range(4)]):
                    return self.board[r][c]

        for r in range(ROWS - 3):
            for c in range(COLS - 3):
                if check_line(*[self.board[r+i][c+i] for i in range(4)]):
                    return self.board[r][c]

        for r in range(3, ROWS):
            for c in range(COLS - 3):
                if check_line(*[self.board[r-i][c+i] for i in range(4)]):
                    return self.board[r][c]

        return 0
