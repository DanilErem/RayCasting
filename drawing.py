import pygame
from settings import *
from ray_casting import ray_casting


class Drawing:
    def __init__(self, sc):
        self.sc = sc
        self.font_fps = pygame.font.SysFont('Arial', 36, bold=True)

    def background(self):
        pygame.draw.rect(self.sc, SKYBLUE, (0, 0, RES_WIDTH, RES_HEIGHT // 2))
        pygame.draw.rect(self.sc, DARKGREY, (0, RES_HEIGHT // 2, RES_WIDTH, RES_HEIGHT // 2))

    def world(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font_fps.render(display_fps, 0, ORANGE)
        self.sc.blit(render, fps_pos)
