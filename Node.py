import numpy as np


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

    def __eq__(self, other):
        return self.state == other.state

    def heuristic(self, goal_states):
        mh_distances = np.array([(abs(state.x - self.state.x) + abs(state.y - self.state.y)) for state in goal_states])
        return mh_distances.min()

