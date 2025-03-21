import pygame
from constants import SHOT_RADIUS

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_check(self, other_shape):
        reach = self.radius + other_shape.radius
        distance = self.position.distance_to(other_shape.position)
        if distance <= reach:
            return True
        else:
            return False
