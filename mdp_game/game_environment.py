import numpy as np

class TicTacToeMDP:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)  # 0: empty, 1: player, -1: AI
        self.states = []
        self.actions = [(i, j) for i in range(3) for j in range(3)]  # All possible positions
        self.rewards = {}

    def is_winner(self, player):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all([self.board[i, j] == player for j in range(3)]) or all([self.board[j, i] == player for j in range(3)]):
                return True
        if all([self.board[i, i] == player for i in range(3)]) or all([self.board[i, 2-i] == player for i in range(3)]):
            return True
        return False

    def get_possible_actions(self):
        return [(i, j) for i, j in self.actions if self.board[i, j] == 0]

    def update_state(self, action, player):
        self.board[action] = player
