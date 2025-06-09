class MyAgent:
    def __init__(self):
        # Initialize any necessary variables here
        pass

    def act(self, state):
        # Implement your agent's decision-making logic here
        # `state` contains information about the current environment
        # Return an action (e.g., accelerate, brake, turn left/right)
        if state['speed'] < 10:
            return 'accelerate'
        elif state['distance_to_wall'] < 5:
            return 'brake'
        else:
            return 'turn_left'
