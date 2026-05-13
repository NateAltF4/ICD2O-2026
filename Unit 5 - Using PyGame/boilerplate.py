import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("...")

# ====================
#    MAIN GAME LOOP
# ====================

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()