import pygame

def scoreBoard():
        font = pygame.font.Font(None, 36)
        scoreBoard_text = font.render(f"Score: {score}", True, (255, 255, 0))
        screen.blit(scoreBoard_text, (10,10))