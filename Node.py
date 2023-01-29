import numpy as np
import math


class Node:
    parent = None
    state = None
    action = None
    path_cost = None
    node_count = 0

    def __init__(self, parent, state, action, path_cost):
        self.parent = parent
        self.state = state
        self.action = action
        self.path_cost = path_cost

    def __eq__(self, other):
        return self.state == other.state

    def heuristic(self, goal_states, heuristics):
        if heuristics == '1':
            mh_distances = np.array(
                [(abs(state.x - self.state.x) + abs(state.y - self.state.y)) for state in goal_states]
            )
            return mh_distances.min()
        elif heuristics == '2':
            distances = np.array(
                [(math.sqrt(math.pow(state.x - self.state.x, 2) + math.pow(state.y - self.state.y, 2))) for state in
                 goal_states]
            )
            return distances.min()


