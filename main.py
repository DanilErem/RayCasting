import pygame
import math
from settings import *
from player import Player
from map import world_map
from ray_casting import ray_casting
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((RES_WIDTH, RES_HEIGHT))
clock = pygame.time.Clock()

player = Player()
drawing = Drawing(sc)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    player.movement()

    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)

    # pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
    # pygame.draw.line(sc, GREEN, (int(player.x), int(player.y)), (player.x+RES_WIDTH*math.cos(player.angle),
    #                                                              player.y+RES_WIDTH*math.sin(player.angle)))
    #
    # for x, y in world_map:
    #     pygame.draw.rect(sc, PURPLE, (x, y, TILE, TILE), 2)

    pygame.display.flip()
    clock.tick(FPS)
