class Node:
    parent = None
    state = None
    action = None
    path_cost = None

    def __init__(self, parent, state, action, path_cost):
        self.parent = parent
        self.state = state
        self.action = action
        self.path_cost = path_cost

