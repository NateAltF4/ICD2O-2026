import pygame
import sys
# --- setup ---
pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Test: Move the Square")
clock = pygame.time.Clock()
# --- game objects ---
player = pygame.Rect(400, 250, 50, 50)  # x, y, w, h
speed = 5
# --- main loop ---
running = True
while running:
    # events (quit, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # input (held keys)
    keys = pygame.key.get_pressed()
    dx = dy = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dy -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dy += speed
    # update (with simple bounds)
    player.x = player.x + dx
    player.y = player.y + dy

    if player.x == 0:
        player.x = WIDTH - player.width
    elif player.x == WIDTH - player.width:
        player.x = 0

    if player.y == 0:
        player.y = HEIGHT - player.height
    elif player.y == HEIGHT - player.height:
        player.y = 0

    # draw
    screen.fill((25, 25, 25))          # background
    pygame.draw.rect(screen, (0, 200, 255), player)  # player square
    pygame.display.flip()
    clock.tick(60)  # 60 FPS
pygame.quit()
sys.exit()
