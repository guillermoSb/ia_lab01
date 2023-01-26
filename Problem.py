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
    visited = None
    algorithm = 0

    def __init__(self, initial_state, goal_states, grid, algorithm = 'bfs'):
        self.initial_state = initial_state
        self.goal_states = goal_states
        self.grid = grid
        self.algorithm = algorithm

    def solve(self):
        initial_node = Node(None, self.initial_state, None, 0)
        frontier = [initial_node]
        explored = set()
        it = 0
        while True:
            if len(frontier) == 0:
                return None
            # Choice
            node = None

            if self.algorithm == 'bfs':
                # BFS
                node = self.remove_choice_bfs(frontier)
            elif self.algorithm == 'dfs':
                # DFS
                node = self.remove_choice_dfs(frontier)
            else:
                # A*
                node = self.remove_choice(frontier)
            # Test
            if self.goal_test(node.state):
                print("Problem solved in: ", it, "iterations")
                self.visited = explored
                return node

            # Expand
            explored.add((node.state.x, node.state.y))
            for action in self.action(node.state):
                child = self.child_node(node, action)

                if child.path_cost == math.inf:
                    continue
                # Validate that the child is not on the frontier
                child_in_frontier = False
                for i in range(0, len(frontier)):
                    if frontier[i].state == child.state:
                        child_in_frontier = True

                if not child_in_frontier and (child.state.x, child.state.y) not in explored:
                    frontier.insert(0, child)
            it += 1



    def remove_choice(self, frontier):

        min_cost = math.inf
        idx = None
        for path_idx in range(0, len(frontier)):
            fn = (frontier[path_idx].heuristic(self.goal_states) + frontier[path_idx].path_cost)
            if fn < min_cost:
                idx = path_idx
                min_cost = fn
        if idx is not None:
            return frontier.pop(idx)
        return None

    def remove_choice_bfs(self, frontier):
        min_cost = math.inf
        idx = None

        for path_idx in range(0, len(frontier)):
            fn = frontier[path_idx].node_count
            if fn < min_cost:
                idx = path_idx
                min_cost = fn
        if idx is not None:
            return frontier.pop(idx)

        return None

    def remove_choice_dfs(self, frontier):
        max_cost = 0
        idx = None
        if len(frontier) == 1:
            return frontier.pop(0)
        for path_idx in range(0, len(frontier)):
            fn = frontier[path_idx].node_count
            if fn > max_cost:
                idx = path_idx
                max_cost = fn
        if idx is not None:
            return frontier.pop(idx)
        return None

    def action(self, s):
        return s.possible_actions(self)

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
        node = Node(parent, s, action, path_cost)
        if node.parent is not None:
            node.node_count = node.parent.node_count + 1
        return node