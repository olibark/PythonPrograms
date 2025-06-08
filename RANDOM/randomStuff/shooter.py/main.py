import pygame
import random
import time


last_click = time.time()
time_between_clicks = 0
current_time = time.time()
noclicks = 0
scorer = 0
totaltime = 0
mouse_clicks = 0
misses = mouse_clicks - scorer


def screen_width():
    return 1000
def screen_height():
    return 1000
def random_colour():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
def circle():
    pygame.draw.circle(background, (255, 255, 255), (circle_pos), 30)
def screen():
    background.fill((0, 0, 0))
def score():
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(scorer), True, (255, 255, 255))
    background.blit(text, (10, 10))
def display_time():
    if noclicks>0:
        font = pygame.font.Font(None, 36)
        text = font.render(f"Time between hits: {time_between_clicks:.2f}", True, (255, 255, 255))
        background.blit(text, (10, 50))
        mean_time = totaltime/ noclicks
        text = font.render(f"Mean time between hits: {mean_time:.2f}", True, (255, 255, 255))
        background.blit(text, (10, 90))
        text = font.render(f"clicks: {mouse_clicks}", True, (255, 255, 255))
        background.blit(text, (10, 130))

        text = font.render(f"Misses: {misses}", True, (255, 255, 255))
        background.blit(text, (10, 180))


circle_pos = [250, 250]
pygame.init()
game_run = True

background = pygame.display.set_mode((screen_width(), screen_height())) 
pygame.display.set_caption("Ray Tracing")

while game_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
                pygame.quit()  
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                mouse_clicks = mouse_clicks + 1 
                if ((mousex - circle_pos[0])**2 + (mousey - circle_pos[1])**2) <= 30**2:
                    circle_pos [0] = random.randint(0, screen_width())
                    circle_pos [1] = random.randint(0, screen_height())
                    current_time = time.time()
                    time_between_clicks = current_time - last_click
                    last_click = current_time
                    scorer += 1
                    noclicks += 1
                    totaltime = totaltime + time_between_clicks

        screen()
        circle()
        score()
        display_time()
        pygame.display.flip()
        

pygame.quit()
            

