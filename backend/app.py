from flask import Flask, request, jsonify
from flask_cors import CORS
from game import ConnectFour
from heuristic import heuristic
from player import AIPlayer

app = Flask(__name__)
CORS(app)  # Autorise l’accès depuis React

ai_player = AIPlayer(2, depth=5, heuristic=heuristic)

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    board_data = data['board']
    current_player = data['player']
    column = data['column']

    game = ConnectFour()
    game.board = board_data
    game.current_player = current_player

    if game.board[0][column] != 0:
        return jsonify({'error': 'Invalid move'}), 400

    game.make_move(column)
    winner = game.check_winner()
    draw = game.is_full() and winner == 0

    if winner == 0 and not draw:
        game.switch_player()
        ai_move = ai_player.get_move(game)
        game.make_move(ai_move)

    result = {
        'new_board': game.board,
        'winner': game.check_winner(),
        'draw': game.is_full() and game.check_winner() == 0
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
