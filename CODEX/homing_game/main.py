import pygame
import math
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Homing Missile Game")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 128, 0)

# Player settings
PLAYER_SIZE = 30
PLAYER_SPEED = 5
player_pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)

MISSILE_SIZE = 10
MISSILE_SPEED = random.uniform(1, 3)  # Random speed for missiles
MISSILE_LIFETIME = 15  # seconds
EXPLOSION_RADIUS = 60  # pixels

# Store each missile as a dict with position and spawn_time
missiles = [{
    "pos": pygame.Vector2(WIDTH // 2, HEIGHT - 50),
    "spawn_time": time.time()
}]

# Game state
running = True
font = pygame.font.SysFont(None, 48)
start_time = time.time()
next_missile_time = start_time + 10  # First extra missile after 10 seconds

def draw_player(pos):
    pygame.draw.rect(screen, GREEN, (pos.x, pos.y, PLAYER_SIZE, PLAYER_SIZE))

def draw_missile(pos):
    pygame.draw.circle(screen, RED, (int(pos.x), int(pos.y)), MISSILE_SIZE)

def draw_explosion(pos):
    pygame.draw.circle(screen, ORANGE, (int(pos.x), int(pos.y)), EXPLOSION_RADIUS, 4)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_pos.x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player_pos.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player_pos.y += PLAYER_SPEED

    # Clamp player within screen
    player_pos.x = max(0, min(WIDTH - PLAYER_SIZE, player_pos.x))
    player_pos.y = max(0, min(HEIGHT - PLAYER_SIZE, player_pos.y))

    # Add a new missile every 10 seconds
    current_time = time.time()
    if current_time >= next_missile_time:
        missiles.append({
            "pos": pygame.Vector2(WIDTH // 2, HEIGHT - 50),
            "spawn_time": current_time
        })
        next_missile_time += 10

    screen.fill(BLACK)
    draw_player(player_pos)

    # Missile movement and explosion logic
    hit = False
    player_center = player_pos + pygame.Vector2(PLAYER_SIZE / 2, PLAYER_SIZE / 2)
    exploded_missiles = []

    for missile in missiles:
        missile_age = current_time - missile["spawn_time"]
        if missile_age >= MISSILE_LIFETIME:
            # Draw explosion
            draw_explosion(missile["pos"])
            # Check if player is in explosion radius
            if missile["pos"].distance_to(player_center) < EXPLOSION_RADIUS:
                hit = True
            exploded_missiles.append(missile)
        else:
            # Move missile
            direction = player_center - missile["pos"]
            if direction.length() != 0:
                direction = direction.normalize() * random.uniform(MISSILE_SPEED, MISSILE_SPEED * 1.5)
            missile["pos"] += direction
            draw_missile(missile["pos"])
            # Direct collision with missile
            if missile["pos"].distance_to(player_center) < PLAYER_SIZE / 2 + MISSILE_SIZE:
                hit = True

    # Remove exploded missiles
    for missile in exploded_missiles:
        missiles.remove(missile)

    if hit:
        text = font.render("Game Over", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False
    else:
        pygame.display.flip()

    clock.tick(60)

pygame.quit()