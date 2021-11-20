import esper as ecs
import pyglet
import pyglet.gl as gl

from src.ecs.components.physics_components import RigidBody
from src.helpers import render_hull_from_vertices

class RigidBodyRenderSystem(ecs.Processor):

    def process(self, dt, game):
        for ent, (rigid_body,) in self.world.get_components(RigidBody):
            poly = rigid_body.poly
            position = rigid_body.body.position
            vertices = poly.get_vertices()

            gl.glPushMatrix()
            gl.glTranslatef(position[0], position[1], 0)
            render_hull_from_vertices(vertices)
            gl.glPopMatrix()
            
