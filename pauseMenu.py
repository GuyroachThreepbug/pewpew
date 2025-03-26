from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame


def paused(screen, is_paused):
    font = pygame.font.Font(None, 74)
    text_surface = font.render("Paused - Press P to Resume or Q to quit", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    while is_paused == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Resume game
                    is_paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()
        screen.fill((0, 0, 0))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
    return is_paused