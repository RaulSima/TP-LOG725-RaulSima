from src.ecs.system import System

class PhysicsSystem(System):

    def execute(self, entity):
        velocity = entity.searchComponent("velocity")
        position = entity.searchComponent("position")
        position.x += velocity.x
        position.y += velocity.y