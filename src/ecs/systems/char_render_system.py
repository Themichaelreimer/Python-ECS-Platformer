import esper as ecs
import pyglet
from src.ecs.components.physics_components import RigidBody
from src.ecs.components.common_components import Transform, Char

class CharRenderSystem(ecs.Processor):

    labels = {}

    # Note: Pretty sure this is a memory leak until I can find a way to subscribe to entities being deleted
    def process(self, dt, game):
        for ent, (rigid_body, ch) in self.world.get_components(RigidBody, Char):
            if ent in self.labels:
                #print(f"{rigid_body.body.position.x},{rigid_body.body.position.y}")
                self.labels[ent].x = rigid_body.body.position.x
                self.labels[ent].y = rigid_body.body.position.y
                self.labels[ent].font_size = ch.size
            else:
                self.labels[ent] = pyglet.text.Label(
                    ch.char,
                    font_size=ch.size,
                    x=rigid_body.body.position.x,
                    y=rigid_body.body.position.y, 
                    )
            self.labels[ent].draw()

