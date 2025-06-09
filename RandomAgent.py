import random

class RandomAgent:
    def __init__(self):
        # Initialize any necessary variables here
        pass

    def act(self, state):
        # Implement your agent's decision-making logic here
        actions = ['accelerate', 'brake', 'turn_left', 'turn_right']
        return random.choice(actions)
