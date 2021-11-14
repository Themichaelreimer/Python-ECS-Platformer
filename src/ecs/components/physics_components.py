from dataclasses import dataclass as component
from typing import Tuple
import pymunk


class RigidBody:
    
    def __init__(self, space, position:Tuple[float,float], size:float):
        self.body =  pymunk.Body()
        self.body.position = position
        self.poly = pymunk.Poly.create_box(self.body, (size, size))
        self.poly.friction = 0.5
        self.poly.mass = 1
        space.add(self.body, self.poly)

 