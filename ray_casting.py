import math
import pygame
from settings import *
from map import world_map


# def ray_casting(sc, player_pos, player_angle):
#     cur_angle = player_angle - FOV / 2
#     xo, yo = player_pos
#     for ray in range(NUM_RAYS):
#         sin_a = math.sin(cur_angle)
#         cos_a = math.cos(cur_angle)
#         for depth in range(MAX_DEPTH):
#             x = xo + depth * cos_a
#             y = yo + depth * sin_a
#             # pygame.draw.line(sc, DARKGREY, player_pos, (x, y), 2)
#             if (x // TILE * TILE, y // TILE * TILE) in world_map:
#                 depth *= math.cos(player_angle - cur_angle)
#                 proj_heigth = PROJ_COEFF / (depth + 1)
#                 c = 255 / (1 + depth * depth * 0.00002)
#                 color = (c, c, c)
#                 pygame.draw.rect(sc, color, (ray * SCALE, RES_HEIGHT//2 - proj_heigth // 2, SCALE, proj_heigth))
#                 break
#         cur_angle += DELTA_ANGEL
def mapping(a, b):
    return  (a // TILE) * TILE, (b // TILE) * TILE

def ray_casting(sc, player_pos, player_angle):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - FOV/2
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)


