from PIL import Image
import numpy as np
from AgentState import AgentState



BLACK = (0,0,0,255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)


class Map:
    GRID_SIZE = 200
    map_matrix = []     # Matrix to store the map information
    start_added = False
    start_coords = None
    goal_states = []

    def __init__(self, file_name):
        img = Image.open(file_name)
        width, height = img.size
        if width != height:
            raise Exception("The image must have the same dimensions.")
        for x in range(0, self.GRID_SIZE):
            img_x = (x / self.GRID_SIZE) * width
            col = []
            for y in range(0, self.GRID_SIZE):
                img_y = (y/self.GRID_SIZE) * height

                colors = img.getpixel((img_x, img_y))
                r = colors[0]
                g = colors[1]
                b = colors[2]
                color = Map.get_color(r, g, b)
                if color is RED and not self.start_added:
                    self.start_coords = AgentState(x, y)
                    self.start_added = True
                elif color is RED and self.start_added:
                    color = WHITE
                if color is GREEN:
                    if not self.has_near_goal_state(15, x, y):
                        self.goal_states.append(AgentState(x, y))
                col.append(color)
            self.map_matrix.append(col)

    def has_near_goal_state(self, th, x, y):
        new_x = max(0, x - th)
        new_y = max(0, y - th)
        for dx in range(new_x, min(x + th, self.GRID_SIZE)):
            for dy in range(new_y, min(y + th, self.GRID_SIZE)):
                if AgentState(dx, dy) in self.goal_states:
                    return True
        return False

    def draw_path(self, locations):
        for location in locations:
            x,y = (location.x, location.y)
            self.map_matrix[x][y] = (0,0,255,255)

    def draw_visited(self, visited):
        for location in visited:
            x,y = location
            self.map_matrix[x][y] = (0,255,255,255)

    def draw_start(self):
        self.map_matrix[self.start_coords.x][self.start_coords.y] = (255, 0, 0, 255)

    @staticmethod
    def get_color( r, g, b):
        color = np.array([r,g,b])
        red, green, black, white = np.array(RED[0:3]), np.array(GREEN[0:3]), np.array(BLACK[0:3]), np.array(WHITE[0:3])
        if np.array_equal(red,color):
            return RED
        elif np.array_equal(black, color):
            return BLACK
        elif np.array_equal(green, color):
            return GREEN
        elif np.array_equal(white, color):
            return WHITE

        red_diff = abs(np.linalg.norm(color - red))
        black_diff = abs(np.linalg.norm(color - black))
        white_diff = abs(np.linalg.norm(color - white))
        green_diff = abs(np.linalg.norm(color - green))

        min_diff = min(red_diff, black_diff)
        min_diff = min(min_diff, white_diff)
        min_diff = min(min_diff, green_diff)
        if min_diff == red_diff:
            return RED
        elif min_diff == black_diff:
            return BLACK
        elif min_diff == green_diff:
            return GREEN
        elif min_diff == white_diff:
            return WHITE
        return WHITE

    def draw_image(self):
        img = Image.new(mode="RGB", size=(self.GRID_SIZE, self.GRID_SIZE))
        for x in range(0, self.GRID_SIZE):
            for y in range(0, self.GRID_SIZE):
                color = self.map_matrix[x][y]
                img.putpixel((x,y), color)
        img.show()
