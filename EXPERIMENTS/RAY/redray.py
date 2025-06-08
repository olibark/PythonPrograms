import pygame
import sys
import math
run = True 
lx = 500
ly = 500
lw = 10
lh = 10
pygame.init()



screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("RAY")




def draw_light():
    pygame.draw.circle(screen, (255, 255, 5), (50, 50), 10)

def draw_ray():
    centery, centerx = 500, 500
    length = 1000
    for degree in range (0, 360, 8):
        radians = math.radians(degree)
        end_x = centerx + length * math.cos(radians)
        end_y = centery + length * math.sin(radians)
        pygame.draw.line(screen, (255, 0, 0), (centerx, centery,), (end_x, end_y))
    pygame.display.flip()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw_ray()
draw_light()


pygame.quit()
sys.exit()



