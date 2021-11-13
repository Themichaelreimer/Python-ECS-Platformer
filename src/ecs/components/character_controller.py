from dataclasses import dataclass as component
from pyglet.window import key

@component
class CharacterController:
    left: key = key.LEFT
    right: key = key.RIGHT
    jump: key = key.UP
    #down: key = key.DOWN