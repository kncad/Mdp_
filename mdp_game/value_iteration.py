class ValueIteration:
    def __init__(self, mdp, gamma=0.9, theta=0.001):
        self.mdp = mdp
        self.gamma = gamma  # Discount factor
        self.theta = theta  # Threshold for convergence
        self.V = {}  # State values
        self.policy = {}  # Optimal policy

    def value_iteration(self):
        for state in self.mdp.states:
            self.V[state] = 0  # Initialize values to 0 for all states

        while True:
            delta = 0
            for state in self.mdp.states:
                v = self.V[state]
                max_value = float('-inf')
                best_action = None
                for action in self.mdp.get_possible_actions(state):
                    next_state, reward = self.mdp.get_next_state(state, action)
                    value = reward + self.gamma * self.V[next_state]
                    if value > max_value:
                        max_value = value
                        best_action = action
                self.V[state] = max_value
                self.policy[state] = best_action
                delta = max(delta, abs(v - self.V[state]))

            if delta < self.theta:
                break

    def get_optimal_action(self, state):
        return self.policy[state]
