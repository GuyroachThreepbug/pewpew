from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS

class Shot(CircleShape):

	def __init__(self, x, y, radius, velocity):
		super().__init__(x, y, radius)
		self.velocity = velocity if velocity else pygame.Vector2(0, 0)
		self.position = pygame.Vector2(x, y)
		self.radius = SHOT_RADIUS

	def draw(self, screen):
		center_arg = int(self.position.x), int(self.position.y)
		radius = SHOT_RADIUS
		
		pygame.draw.circle(screen, (255, 255, 255), center_arg, radius, 0)
	
	def update(self,dt):
		self.position += self.velocity * dt
