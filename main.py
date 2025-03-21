import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    clip = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroid_group, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (clip, updatable, drawable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT/2, clip=clip)
    Asteroid_Field = AsteroidField()
    asteroid = Asteroid(x=100, y=100, radius=20)
    player.clip = clip

    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroid_group:
            if asteroid.collision_check(player):
                print("Game Over!")
                sys.exit()

        for asteroid in asteroid_group:
            for bullet in clip:
                if asteroid.collision_check(bullet):
                    asteroid.kill()
                    bullet.kill()


        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()