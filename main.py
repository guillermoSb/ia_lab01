from Map import Map
from Problem import Problem
import time

# todo - implement data structures for the A* algorithm
# todo - implement path finding for the A* algorithm

if __name__ == '__main__':
    map = Map('turing.png')
    problem = Problem(map.start_coords,map.goal_states, map)
    start = time.time()
    sol = problem.solve()
    end = time.time()
    locations = []

    if sol is not None:
        while sol.parent is not None:
            locations.append(sol.state)
            sol = sol.parent
        print("Solution time: ", (end - start) * 1000, "ms")
        map.draw_path(locations)
        map.draw_image()






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
