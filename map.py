from settings import *

text_map = [
    'WWWWWWWWWWWW',
    'W...W......W',
    'WW.WW.W.WW.W',
    'W...W...W..W',
    'W.W.....WWWW',
    'W.W.WWW....W',
    'WWW...w.WW.W',
    'WWWWWWWWWWWW',
]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
