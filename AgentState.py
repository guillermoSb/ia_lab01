from AgentAction import AgentAction

class AgentState:
    x, y = None, None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def possible_actions(self, grid_size, actions):
        if self.x == 0:
            idx = next((idx for idx in range(0, len(actions)) if actions[idx].name == "LEFT"), None)
            actions.pop(idx)
        # agent can only go right if the x is lower than the size of the grid
        if self.x >= grid_size - 1:
            idx = next((idx for idx in range(0, len(actions)) if actions[idx].name == "RIGHT"), None)
            actions.pop(idx)
        # agent can't go top if it is on y 0
        if self.y == 0:
            idx = next((idx for idx in range(0, len(actions)) if actions[idx].name == "TOP"), None)
            actions.pop(idx)
        # agent can only go to the bottom if the y is lower than the size of the grid
        if self.y >= grid_size - 1:
            idx = next((idx for idx in range(0, len(actions)) if actions[idx].name == "BOTTOM"), None)
            actions.pop(idx)
        return actions

    def __eq__(self, other):
        return self.x is other.x and self.y is other.y