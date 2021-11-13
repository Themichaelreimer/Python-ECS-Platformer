import esper as ecs
from src.ecs.components.common_components import *
from src.ecs.components.character_controller import CharacterController
from src.ecs.components.physics_components import *

def create_player(game:'GameInstance'):
    world = game.ecs_world
    player = world.create_entity()
    world.add_component(player, RigidBody(game.space, (50,50), 24))
    world.add_component(player, CharacterController())
    world.add_component(player, Char(char="@", size=24))
    return player
