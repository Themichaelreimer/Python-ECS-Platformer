import esper as ecs
from src.ecs.components.physics_components import RigidBody
from src.ecs.components.common_components import Transform

from src.ecs.components.character_controller import CharacterController
from pyglet.window import key

CHARACTER_SPEED  = 20

class CharacterControlSystem(ecs.Processor):
    def process(self, dt, game):
        keys = game.keys
        # TODO: replace tranform with rigidbody component
        for ent, (controller, rb) in self.world.get_components(CharacterController, RigidBody):
            if keys[controller.left]:
                rb.body.apply_force_at_local_point((-CHARACTER_SPEED,0))
            if keys[controller.right]:
                rb.body.apply_force_at_local_point((CHARACTER_SPEED,0))
            if keys[controller.jump]:
                rb.body.velocity.y = CHARACTER_SPEED
            #print(f"Character Transform - Position:({transform.x},{transform.y}) - Scale:({transform.sx},{transform.sy})")