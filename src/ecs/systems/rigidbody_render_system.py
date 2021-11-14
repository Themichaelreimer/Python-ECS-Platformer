import esper as ecs
import pyglet
from src.ecs.components.physics_components import RigidBody

class RigidBodyRenderSystem(ecs.Processor):



    def process(self, dt, game):
        for ent, (rigid_body) in self.world.get_components(RigidBody):
            poly = rigid_body.poly
            import pdb
            pdb.set_trace()
