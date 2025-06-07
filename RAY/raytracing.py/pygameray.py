import pygame as pg

import math

running = True 
circle_pos = 250, 200
light_pos = 250, 250
square_size = 100  # Define the size of the square
pg.init()

background = pg.display.set_mode((1000, 1000)) 

def draw_square():
    pg.draw.rect(background, (255, 255, 255), (circle_pos[0] - square_size // 2, circle_pos[1] - square_size // 2, square_size, square_size))

def draw_lightbulb():
    pg.draw.circle(background, (255, 165, 0), (light_pos), 10)

def draw_ray():
    for i in range(360):
        for length in range(1000):
            end_pos = (light_pos[0] + length * math.cos(math.degrees(i)), light_pos[1] + length * math.sin(math.degrees(i)))
            if check_intersection(light_pos, end_pos):
                pg.draw.line(background, (255, 255, 0), light_pos, end_pos, width=1)
                break
            pg.draw.line(background, (255, 255, 0), light_pos, end_pos, width=1)

def check_intersection(start_pos, end_pos):
    square_corners = [
        (circle_pos[0] - square_size // 2, circle_pos[1] - square_size // 2),
        (circle_pos[0] + square_size // 2, circle_pos[1] - square_size // 2),
        (circle_pos[0] + square_size // 2, circle_pos[1] + square_size // 2),
        (circle_pos[0] - square_size // 2, circle_pos[1] + square_size // 2)
    ]
     
    for i in range(4):
        next_i = (i + 1) % 4
        if line_intersection(start_pos, end_pos, square_corners[i], square_corners[next_i]):
            return True
    return False

def line_intersection(p1, p2, p3, p4):
    def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
    
    return ccw(p1, p3, p4) != ccw(p2, p3, p4) and ccw(p1, p2, p3) != ccw(p1, p2, p4)




while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            circle_pos = pg.mouse.get_pos()
            background.fill((0, 0, 0))
            draw_ray()
    draw_square()
    draw_lightbulb()
    pg.display.flip()
    