import pyglet
from pyglet.gl import *
import pymunk
import esper as ecs
from src.ecs.entity_factory import create_player
import src.level_manager as level_manager

from src.ecs.systems.char_render_system import CharRenderSystem
from src.ecs.systems.character_control_system import CharacterControlSystem


FPS_INTERVAL = 1/60
window = pyglet.window.Window(800,600)
game = None

class GameInstance:
    """
        Essentially a container for references to globals that would be awkward
        to manage other ways
    """

    def __init__(self):
        self.window = window
        self.keys = keys
        self.ecs_world = ecs_world
        self.space = space
        self.platforms = []

def init_ecs_world(game:GameInstance):
    world = game.ecs_world
    world.add_processor(CharacterControlSystem(), 0)
    world.add_processor(CharRenderSystem(), 0)
    create_player(game)

def on_draw(dt):
    window.clear()
    batch = pyglet.graphics.Batch()
    if game:
        game.ecs_world.process(FPS_INTERVAL, game)
        #print_options = pymunk.SpaceDebugDrawOptions()
        #space.debug_draw(print_options)
        space.step(FPS_INTERVAL)

        glBegin(GL_LINES)
        glColor3f(1.0,1.0,1.0)
        for platform in game.platforms:
            glVertex2f(platform.p1[0],platform.p1[1])
            glVertex2f(platform.p2[0],platform.p2[1])
        glEnd()
            #print(f"DRAW PLATFORM: [({platform.p1}) to ({platform.p2})]")
            #pyglet.shapes.Line(platform.p1[0], platform.p1[1], platform.p2[0], platform.p2[1], 4, color=(255,0,0), batch=batch)
    batch.draw()
    


if __name__ == '__main__':
    
    # Keyboard
    keys = pyglet.window.key.KeyStateHandler()
    window.push_handlers(keys)

    ecs_world = ecs.World()
    space = pymunk.Space()
    space.gravity = (0, -981)
    game = GameInstance()

    init_ecs_world(game)
    level_manager.load_level(game)

    pyglet.clock.schedule_interval(on_draw, FPS_INTERVAL)

    pyglet.app.run()
