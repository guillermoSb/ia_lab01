from PIL import Image
import numpy as np




BLACK = (0,0,0,255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)


class Map:
    GRID_SIZE = 200
    map_matrix = []     # Matrix to store the map information
    start_added = False
    start_coords = None
    agent_location = None
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

                r, g, b, _ = img.getpixel((img_x, img_y))
                color = Map.get_color(r, g, b)
                if color is RED and not self.start_added:
                    self.start_coords = (x, y)
                    self.agent_location = self.start_coords
                    self.start_added = True
                elif color is RED and self.start_added:
                    color = WHITE
                if color is GREEN:
                    self.goal_states.append((x,y))
                col.append(color)
            self.map_matrix.append(col)

    def draw_path(self, locations):
        for location in locations:
            x,y = location
            self.map_matrix[x][y] = (0,0,255,255)
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
