import pygame
import sys
import random

pygame.init()
running = True

WIDTH = 800
HEIGHT = 600
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("WALK AROUND")

class Player:
    def __init__(self, image):
        self.character = pygame.image.load(image)
        self.rect = self.character.get_rect()

    def draw_player(self, surface):
        surface.blit(self.character, self.rect)
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

player = Player("RedCircle.png")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-1, 0)
    if keys[pygame.K_RIGHT]:
        player.move(1, 0)
    if keys[pygame.K_UP]:
        player.move(0, -1)
    if keys[pygame.K_DOWN]:
        player.move(0, 1)
    
    if keys[pygame.K_1]:
        canvas.fill((random.randint(0, 255), 
                      random.randint(0, 255), 
                      random.randint(0, 255)))
    else:
        canvas.fill("black")  # Fill with black only if K_1 is not pressed

    player.draw_player(canvas)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
