from flask import Flask, jsonify, render_template, request
from mdp_game.game_environment import TicTacToeMDP
from mdp_game.value_iteration import ValueIteration
import numpy as np

app = Flask(__name__)

# Initialize game MDP
game = TicTacToeMDP()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def make_move():
    data = request.json
    player = data['player']
    action = tuple(data['action'])  # Convert to tuple (row, col)
    
    # Update game board
    game.update_state(action, player)
    
    # Check if player wins or draw
    if game.is_winner(player):
        return jsonify({'result': f'Player {player} wins!'})
    elif not game.get_possible_actions():
        return jsonify({'result': 'Draw'})
    
    # AI move
    vi = ValueIteration(game)
    vi.value_iteration()
    ai_move = vi.get_optimal_action(game.board_to_state())
    game.update_state(ai_move, -player)
    
    # Check if AI wins
    if game.is_winner(-player):
        return jsonify({'result': 'AI wins!', 'ai_move': ai_move})
    
    return jsonify({'ai_move': ai_move})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
