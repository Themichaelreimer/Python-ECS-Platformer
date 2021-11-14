import pymunk
from pymunk.autogeometry import march_hard, march_soft
from typing import Tuple, Sequence, List

from pymunk.shapes import Segment

# 16x16
SAMPLE_ASCII_LEVEL = """
................
................
................
................
..##............
................
................
................
.........###....
#...............
#...............
#..............#
#..............#
#......##....###
################
################
"""
    

def point_at_pos(point) -> float:
    x, y = point
    y = 15-y  # invert y axis
    return float(0<= x <= 15 and 0 <= y <= 15 and (SAMPLE_ASCII_LEVEL.split()[int(y)][int(x)]) == "#")

class Platform:
    thickness=4
    def __init__(self, game, p1:Tuple[int,int], p2:Tuple[int,int]):
        space = game.space

        # Physics object
        #print(f"Segment from {p1} to {p2}")
        self.segment = pymunk.Segment(space.static_body, p1, p2, self.thickness)
        self.segment.friction = 0.5
        self.p1 = p1
        self.p2 = p2
        space.add(self.segment)


def load_level(game):
    #Platform(game, (0,0), (800, 0))
    #Platform(game, (400,50), (800, 50))
    #Platform(game, (0,0), (0, 1000))
    #Platform(game, (800,0), (800, 1000))

    result = []
    pl_set: Sequence[pymunk.autogeometry.PolylineSet] = march_hard(pymunk.BB(0,0,15,15), 16, 16, 0.5, point_at_pos)
    tile_size = 32
    for body in pl_set:
        prev_point = None
        point = None
        for new_point in body:

            # Advance the 2-point window
            prev_point = point
            point = new_point

            # Build Platform
            if point and prev_point:
                result.append(Platform(game, tile_size*prev_point, tile_size*point))
    game.platforms = result
                
            


