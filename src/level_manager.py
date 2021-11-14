import pymunk
from typing import Tuple

class Platform:
    thickness=4
    def __init__(self, game, p1:Tuple[int,int], p2:Tuple[int,int]):
        space = game.space

        # Physics object
        self.segment = pymunk.Segment(space.static_body, p1, p2, self.thickness)
        space.add(self.segment)

        # Graphics object


def load_level(game):
    Platform(game, (0,0), (800, 0))
    Platform(game, (400,50), (800, 50))
    Platform(game, (0,0), (0, 1000))
    Platform(game, (800,0), (800, 1000))

