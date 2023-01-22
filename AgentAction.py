import copy


class AgentAction:
    name = None

    def __init__(self, name,):
        self.name = name

    def result(self, s):
        new_state = copy.copy(s)
        if self.name == "LEFT":
            new_state.x -= 1
        elif self.name == "RIGHT":
            new_state.x += 1
        elif self.name == "TOP":
            new_state.y -= 1
        elif self.name == "BOTTOM":
            new_state.y += 1
        return new_state

    def __eq__(self, other):
        return other.name == self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
