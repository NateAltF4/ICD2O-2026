import pygame

pygame.init()

WIDTH, HEIGHT = 800, 500
GROUND_HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Player:
    def __init__(self):
        self.w = 50
        self.h = 50
        self.jumping = False
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]


running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
    
