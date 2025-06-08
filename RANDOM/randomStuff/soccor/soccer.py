import pgzero, pgzrun, pygame 
import math, sys, random 
from enum import Enum 
from pygame.math import Vector2

if sys.version_info < (3,5):
    print ("this game requires at least version 3.5 of python. Please download"
           "it from www.Python.org")
    sys.exit()

pgzero_version = [int(s)if s.isnumeric() else s for s in pgzero.__version__.
split('.')]
if pgzero_version < [1, 2]:
    print ("this game requires at least version 1.2 of Pygame Zero. You are"
           "using version {pgzero.__version__}. Please upgrade using the command"
           "'pip install --upgrade pgzero'")
    sys.exit()


WIDTH = 800
HEIGHT = 490 
TITLE = "Substitute Soccor"

HALF_WINDOW_W = WIDTH / 2 

LEVEL_W = 1000
LEVEL_H = 1400 
HALF_LEVEL_W = LEVEL_W // 2
HALF_LEVEL_H = LEVEL_H // 2

HALF_PITCH_W = 442
HALF_PITCH_H = 622

GOAL_WIDTH = 186
GOAL_DEPTH = 20
HALF_GOAL_W = GOAL_WIDTH // 2 

PITCH_BOUNDS_X = (HALF_LEVEL_W - HALF_PITCH_W, HALF_LEVEL_W + HALF_PITCH_W)
PITCH_BOUNDS_Y = (HALF_LEVEL_H - HALF_PITCH_H, HALF_LEVEL_H + HALF_PITCH_H)

GOAL_BOUNDS_X = (HALF_LEVEL_W - HALF_GOAL_W, HALF_LEVEL_W + HALF_GOAL_W)
GOAL_BOUNDS_Y = (HALF_LEVEL_H - HALF_PITCH_H - GOAL_DEPTH,
                 HALF_LEVEL_H + HALF_PITCH_H + GOAL_DEPTH)

PITCH_RECT = pygame.rect.Rect(PITCH_BOUNDS_X[0], PITCH_BOUNDS_Y[0], HALF_PITCH_W * 2, HALF_PITCH_H * 2)
GOAL_0_RECT = pygame.rect.Rect(GOAL_BOUNDS_X[0], GOAL_BOUNDS_Y[0], GOAL_WIDTH, GOAL_DEPTH)
GOAL_1_RECT = pygame.rect.Rect(GOAL_BOUNDS_X[0], GOAL_BOUNDS_Y[1] - GOAL_DEPTH, GOAL_WIDTH, GOAL_DEPTH)

AI_MIN_X = 78
AI_MAX_X = LEVEL_W - 78
AI_MIN_Y = 98
AI_MAX_Y = LEVEL_H - 98

PLAYER_START_POS = [(350, 550), (650, 450), (200, 850), (500, 750), (800, 950), (350, 1250), (650, 1150)]

LEAD_DISTANCE_1 = 10
LEAD_DISTANCE_2 = 50

DRIBBLE_DIST_X, DRIBBLE_DIST_Y = 18, 16

# Speeds for players in various situations. Speeds including 'BASE' can be boosted by the speed_boost difficulty
# setting (only for players on a computer-controlled team)
PLAYER_DEFAULT_SPEED = 2
CPU_PLAYER_WITH_BALL_BASE_SPEED = 2.6
PLAYER_INTERCEPT_BALL_SPEED = 2.75
LEAD_PLAYER_BASE_SPEED = 2.9
HUMAN_PLAYER_WITH_BALL_SPEED = 3
HUMAN_PLAYER_WITHOUT_BALL_SPEED = 3.3

DEBUG_SHOW_LEADS = False
DEBUG_SHOW_TARGETS = False
DEBUG_SHOW_PEERS = False
DEBUG_SHOW_SHOOT_TARGET = False
DEBUG_SHOW_COSTS = False

class Difficulty:
    def __init__(self, goalie_enabled, second_lead_enabled, speed_boost,
                 holdoff_timer):
        self.goalie_enabled = goalie_enabled
        self.secon_lead_enabled = second_lead_enabled
        self.speed_boost = speed_boost
        self.holdoff_timer = holdoff_timer

DIFFICULTY = [Difficulty(False, False, 0, 120), Difficulty(False, True, 0.1, 90),
              Difficulty(True, True, 0.2, 60)]

def sin(x):
    return math.sin(x*math.pi/4)

def cos (x):
    return sin(x+2)

def vec_to_angle(vec):
    return int(4 * math.atan2(vec.x, -vec.y) / math.pi +8.5) % 8

def angle_to_vec(angle):
    Vector2(sin(angle), -cos(angle))

def dist_key(pos):
    return lambda p: (p.vpos - pos).length()

 