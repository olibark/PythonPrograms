import pygame as pg
import math
running = True 
circle_pos = 500, 500
light_pos = 300, 500
square_size = 60
pg.init()


background = pg.display.set_mode((1000, 1000)) 
def draw_circle():
    pg.draw.rect(background, (255, 255, 255), (circle_pos[0] - square_size // 2, circle_pos[1] - square_size // 2, square_size, square_size))
def draw_lightbulb():
    pg.draw.circle(background, (255, 165, 0), (light_pos), 10)
def draw_ray():
    for i in range (1000):
        end_pos = (light_pos[0] + 1000 * math.cos(math.degrees(i)), light_pos[1] + 1000 * math.sin(math.degrees(i)))
        pg.draw.line(background, (255, 255, 255), light_pos, end_pos)
        if check(light_pos, end_pos):
             print (f"Ray {i} intersected with the square")
def check(start_pos, end_pos):
     square_corners =[
        (circle_pos[0] - square_size // 2, circle_pos[1] - square_size // 2),
        (circle_pos[0] + square_size // 2, circle_pos[1] - square_size // 2),
        (circle_pos[0] + square_size // 2, circle_pos[1] + square_size // 2),
        (circle_pos[0] - square_size // 2, circle_pos[1] + square_size // 2)
     ]
     
     for i in range (4):
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
                game_run = False
                pg.quit()  
    draw_circle()
    draw_lightbulb()
    draw_ray()
    pg.display.flip()