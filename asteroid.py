from circleshape import CircleShape
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(50, 50)
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        center_arg = int(self.position.x), int(self.position.y)
        radius = int(self.radius)

        pygame.draw.circle(screen, (255, 255, 255), center_arg, radius, 2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        else:
            random_angle = random.uniform(20, 50)
            new_vector1 = self.velocity.rotate(random_angle)
            new_vector2 = self.velocity.rotate(-random_angle)
            new_Asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            radius = new_Asteroid_radius

            new_Asteroid1 = Asteroid(self.position.x, self.position.y, radius)
            new_Asteroid1.velocity = new_vector1 * 1.2

            new_Asteroid2 = Asteroid(self.position.x, self.position.y, radius)
            new_Asteroid2.velocity = new_vector2 * 1.2

            return new_Asteroid1, new_Asteroid2