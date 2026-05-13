import pygame

pygame.init()

# Game settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GROUND_Y = 500  # The y-coordinate of the ground
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Jump")
clock = pygame.time.Clock()

# Player variables
player_width, player_height = 60, 60
player_x = 400
player_y = 100
player_vel_y = 0
gravity = 0.8
jump_height = -3  # Initial upward velocity, negative moves up

is_jumping = False

run = True
while run:
    clock.tick(60) # Limits the game to 60 FPS

    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            # Only allow jumping if the player is on the ground
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                player_vel_y += jump_height # Set initial jump velocity

    # 2. Game Logic (Applying physics)
   
    player_vel_y += gravity  # Apply gravity to velocity
    player_y += player_vel_y # Apply velocity to position

        # Check for ground collision
    if player_y >= GROUND_Y - player_height:
        player_y = GROUND_Y - player_height # Place player firmly on the ground
        is_jumping = False
        player_vel_y = 0 # Reset vertical velocity

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:  player_x += 5
    if keys[pygame.K_a]:  player_x -= 5

    # 3. Drawing
    screen.fill((0, 0, 64)) # Fill background with dark blue
    pygame.draw.rect(screen, (64, 64, 64), (0, GROUND_Y +20, 20, SCREEN_HEIGHT - GROUND_Y))
    pygame.draw.rect(screen, (64, 64, 64), (0, GROUND_Y, SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_Y)) # Draw ground
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_width, player_height)) # Draw player

    # Update the display
    pygame.display.flip()

pygame.quit()
