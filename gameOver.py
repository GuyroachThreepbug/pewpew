
import pygame

def ded(screen):

    font = pygame.font.Font(None, 74)
    text_surface = font.render("Game Over - Press R to Restart or Q to Quit", True, (255, 0, 0))
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))


    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart game
                    return "restart"
                if event.key == pygame.K_q:  # Quit game
                    pygame.quit()
                    exit()

        # Fill screen with black
        screen.fill((0, 0, 0))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()