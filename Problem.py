import copy
import math

from Map import BLACK, GREEN
from Node import Node


class Problem:
    initial_state = None
    goal_states = None
    grid = None
    actions = ["LEFT", "RIGHT", "TOP", "BOTTOM"]


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
            explored.add(node.state)
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

                if not child_in_frontier and child.state not in explored:
                    frontier.insert(0, child)
                elif lower_cost is not None:
                    frontier[lower_cost] = child




    def action(self, s):
        agent_x, agent_y = s
        possible_actions = ["LEFT", "RIGHT", "TOP", "BOTTOM"]
        # Agent cant go left if it is on x 0
        if agent_x == 0:
            idx = possible_actions.index("LEFT")
            possible_actions.pop(idx)
        # Agent can only go right if the x is lower than the size of the grid
        if agent_x >= self.grid.GRID_SIZE - 1:
            idx = possible_actions.index("RIGHT")
            possible_actions.pop(idx)
        # Agent cant go top if it is on y 0
        if agent_y == 0:
            idx = possible_actions.index("TOP")
            possible_actions.pop(idx)
        # Agent can only go to the bottom if the y is lower than the size of the grid
        if agent_y >= self.grid.GRID_SIZE - 1:
            idx = possible_actions.index("BOTTOM")
            possible_actions.pop(idx)

        return possible_actions


    def result(self, s, a):

        new_state = list(copy.copy(s))
        if a == "LEFT":
            new_state[0] -= 1
        elif a == "RIGHT":
            new_state[0] += 1
        elif a == "TOP":
            new_state[1] -= 1
        elif a == "BOTTOM":
            new_state[1] += 1
        return (new_state[0], new_state[1])


    def goal_test(self, s):
        if s in self.goal_states:
            print(s)
            print(self.goal_states)
            return True
        return False


    def path_cost(self, p):
        # path item -> [s, a, s1]
        cost = 0
        for path_item in p:
            cost += self.step_cost(path_item[0], path_item[1], path_item[2])
        return cost

    def step_cost(self, s, a):
        new_state = self.result(s, a)
        agent_x, agent_y = new_state
        # Cannot go to a BLACK node
        if self.grid.map_matrix[agent_x][agent_y] == BLACK:
            return math.inf
        return 1

    def child_node(self, parent, action):
        s = self.result(parent.state, action)
        path_cost = parent.path_cost + self.step_cost(parent.state, action)
        return Node(parent, s, action, path_cost)
