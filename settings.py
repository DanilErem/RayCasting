import math

# Game Settings
RES_WIDTH = 1200
RES_HEIGHT = 800
FPS = 60

# Map Settings
TILE = 100

# Ray Casting
FOV = math.pi / 3
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGEL = FOV/NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(FOV/2))
PROJ_COEFF = 3 * DIST * TILE
SCALE = RES_WIDTH // NUM_RAYS

# Draw Settings
fps_pos = (RES_WIDTH - 65, 10)

# Player Settings
player_pos = (RES_WIDTH//2, RES_HEIGHT//2)
player_angle = 0
player_speed = 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 220)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
DARKGREY = (110, 110, 110)
PURPLE = (120, 0, 120)
ORANGE = (210, 100, 0)
SKYBLUE = (0, 186, 255)
