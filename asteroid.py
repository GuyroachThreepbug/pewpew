from circleshape import CircleShape
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

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
