
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def paused(screen):

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 74)
    text_surface = font.render("Paused - Press P to Resume", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    is_paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Resume game
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()
        # Fill screen with a dimmed background
        screen.fill((0, 0, 0))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()