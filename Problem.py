class Problem:
    initial_state = None
    goal_states = None

    def __init__(self, initial_state, goal_states):
        self.initial_state = initial_state
        self.goal_states = goal_states

    def action(self, s):
        pass

    def result(self, s, a):
        pass

    def goal_test(self, s):
        pass

    def path_cost(self, p):
        cost = 0
        return cost


    def step_cost(self, s, a, s1):
        pass
