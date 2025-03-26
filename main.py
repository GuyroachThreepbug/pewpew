import pygame
import sys
import random
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
from gameOver import ded
from pauseMenu import paused


def main():
    pygame.init()
    pygame.font.init()

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

    score = 0
    points = 10

    dt = 0



    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    game_over = False
    is_paused = False

    while True:
        font = pygame.font.Font(None, 36)
        scoreBoard_text = font.render(f"Score: {score}", True, (255, 255, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    is_paused = True
                    paused(screen, is_paused)


        else:

            updatable.update(dt)

            for asteroid in asteroid_group:
                if asteroid.collision_check(player):
                    ded(screen)

            for asteroid in asteroid_group:
                for bullet in clip:
                    if asteroid.collision_check(bullet):
                        asteroid.split()
                        bullet.kill()
                        score += points


        screen.fill((0,0,0))
        screen.blit(scoreBoard_text, (10,10))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()