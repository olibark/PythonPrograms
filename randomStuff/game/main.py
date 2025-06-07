import pygame
import sys
import random
pygame.init()
running = True

colourArr = [random.randint(0, 255), 
                    random.randint(0, 255), 
                    random.randint(0, 255)]

WIDTH = 800
HEIGHT = 600
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("WALK AROUND")

class Player:
    def __init__(self, image):
        self.playerID = None
        self.character = (pygame.image.load("RedCircle.png"))
        self.rect = self.character.get_rect()

    def drawPLayer(self, surface):
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
    
    if keys[pygame.K_p]:
        colourArr = [random.randint(0, 255), 
                    random.randint(0, 255), 
                    random.randint(0, 255)]
    else:
        canvas.fill(colourArr)
    player.drawPLayer(canvas)
    
    clock.tick(60)

    pygame.display.flip()
pygame.quit()
sys.exit()





