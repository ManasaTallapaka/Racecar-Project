class RuleAgent:
    def __init__(self):
        # Initialize any necessary variables here
        self.speed_threshold = 10
        self.wall_distance_threshold = 5

    def act(self, state):
        # Implement your agent's decision-making logic here
        if state['speed'] < self.speed_threshold:
            return 'accelerate'
        elif state['distance_to_wall'] < self.wall_distance_threshold:
            return 'brake'
        elif state['track_position'] < 0.5:
            return 'turn_right'
        else:
            return 'turn_left'
