from Map import Map
from Problem import Problem
import time
import sys


# todo - implement data structures for the A* algorithm
# todo - implement path finding for the A* algorithm

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("No se han enviado todos los campos. Revise el README.md")
        exit()
    file = sys.argv[1]
    algorithm = sys.argv[2]
    if algorithm not in ['bfs', 'dfs', 'as']:
        print("El algoritmo ingresado no es valido. Opciones: bfs, dfs, as")
        exit()
    map = Map(file)
    problem = Problem(map.start_coords,map.goal_states, map, algorithm)
    start = time.time()
    sol = problem.solve()
    end = time.time()
    locations = []
    visited = None

    if sol is not None:
        path_cost = sol.path_cost
        visited = problem.visited
        while sol.parent is not None:
            locations.append(sol.state)
            sol = sol.parent
        print("Solution time: ", (end - start) * 1000, "ms")
        print("Solution cost: ", path_cost)
        map.draw_visited(visited)
        map.draw_path(locations)
        map.draw_start()
        map.draw_image()







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
