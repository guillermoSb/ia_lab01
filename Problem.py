import copy
import math

import numpy as np

from Map import BLACK, GREEN
from Node import Node
from AgentAction import AgentAction


class Problem:
    initial_state = None
    goal_states = None
    grid = None
    actions = [AgentAction("LEFT"), AgentAction("RIGHT"), AgentAction("TOP"), AgentAction("BOTTOM")]

    def __init__(self, initial_state, goal_states, grid):
        self.initial_state = initial_state
        self.goal_states = goal_states
        self.grid = grid

    def solve(self):
        initial_node = Node(None, self.initial_state, None, 0)
        frontier = [initial_node]
        explored = set()
        while True:
            if len(frontier) == 0:
                return None
            node = frontier.pop()
            if self.goal_test(node.state):
                return node
            explored.add((node.state.x, node.state.y))
            for action in self.action(node.state):
                child = self.child_node(node, action)
                if child.path_cost == math.inf:
                    continue
                child_in_frontier = False
                lower_cost = None
                for i in range(0, len(frontier)):
                    if frontier[i].state == child.state:
                        child_in_frontier = True

                    if frontier[i].path_cost > child.path_cost:
                        lower_cost = i

                if not child_in_frontier and (child.state.x, child.state.y) not in explored:
                    frontier.insert(0, child)
                elif lower_cost is not None:
                    print(child)
                    frontier[lower_cost] = child

    def action(self, s):
        return s.possible_actions(self.grid.GRID_SIZE, copy.copy(self.actions))

    def result(self, s, a):
        new_state = a.result(s)
        return new_state

    def goal_test(self, s):

        if s in self.goal_states:
            return True
        return False

    def path_cost(self, p):
        cost = 0
        for path_item in p:
            cost += self.step_cost(path_item[0], path_item[1], path_item[2])
        return cost

    def step_cost(self, s, a):
        new_state = self.result(s, a)
        agent_x, agent_y = new_state.x, new_state.y
        # Cannot go to a BLACK node
        if self.grid.map_matrix[agent_x][agent_y] == BLACK:
            return math.inf
        return 1

    def child_node(self, parent, action):
        s = self.result(parent.state, action)
        path_cost = parent.path_cost + self.step_cost(parent.state, action)
        return Node(parent, s, action, path_cost)