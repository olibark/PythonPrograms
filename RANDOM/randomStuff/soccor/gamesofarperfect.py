import pgzero, pgzrun, pygame
import math, sys, random
from enum import Enum
from pygame.math import Vector2

# Check Python version number. sys.version_info gives version as a tuple, e.g. if (3,7,2,'final',0) for version 3.7.2.
# Unlike many languages, Python can compare two tuples in the same way that you can compare numbers.
if sys.version_info < (3,5):
    print("This game requires at least version 3.5 of Python. Please download it from www.python.org")
    sys.exit()

# Check Pygame Zero version. This is a bit trickier because Pygame Zero only lets us get its version number as a string.
# So we have to split the string into a list, using '.' as the character to split on. We convert each element of the
# version number into an integer - but only if the string contains numbers and nothing else, because it's possible for
# a component of the version to contain letters as well as numbers (e.g. '2.0.dev0')
# We're using a Python feature called list comprehension - this is explained in the Bubble Bobble/Cavern chapter.
pgzero_version = [int(s) if s.isnumeric() else s for s in pgzero.__version__.split('.')]
if pgzero_version < [1,2]:
    print("This game requires at least version 1.2 of Pygame Zero. You have version {0}. Please upgrade using the command 'pip3 install --upgrade pgzero'".format(pgzero.__version__))
    sys.exit()

WIDTH = 800
HEIGHT = 480
TITLE = "Substitute Soccer"

HALF_WINDOW_W = WIDTH / 2

# Size of level, including both the pitch and the boundary surrounding it
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
    def __init__(self, goalie_enabled, second_lead_enabled, speed_boost, holdoff_timer):
        self.goalie_enabled = goalie_enabled

        # When a player has the ball, either one or two players will be chosen from the other team to try to intercept
        # the ball owner. Those players will have their 'lead' attributes set to a number indicating how far ahead of the
        # ball they should try to run. (If they tried to go to where the ball is currently, they'd always trail behind)
        # This attribute determines whether there should be one or two lead players
        self.second_lead_enabled = second_lead_enabled

        # Speed boost to apply to CPU-team players in certain circumstances
        self.speed_boost = speed_boost

        # Hold-off timer limits rate at which computer-controlled players can pass the ball
        self.holdoff_timer = holdoff_timer

DIFFICULTY = [Difficulty(False, False, 0, 120), Difficulty(False, True, 0.1, 90), Difficulty(True, True, 0.2, 60)]

# Custom sine/cosine functions for angles of 0 to 7, where 0 is up,
# 1 is up+right, 2 is right, etc.
def sin(x):
    return math.sin(x*math.pi/4)

def cos(x):
    return sin(x+2)

# Convert a vector to an angle in the range 0 to 7
def vec_to_angle(vec):
    # todo explain a bit
    # https://gamedev.stackexchange.com/questions/14602/what-are-atan-and-atan2-used-for-in-games
    return int(4 * math.atan2(vec.x, -vec.y) / math.pi + 8.5) % 8

# Convert an angle  in the range 0 to 7 to a direction vector. We use -cos rather than cos as increasing angles move
# in a clockwise rather than the usual anti-clockwise direction.
def angle_to_vec(angle):
    return Vector2(sin(angle), -cos(angle))

# Used when calling functions such as sorted and min.
# todo explain more
# p.vpos - pos results in a Vector2 which we can get the length of, giving us
# the distance between pos and p.vpos
def dist_key(pos):
    return lambda p: (p.vpos - pos).length()

# Turn a vector into a unit vector - i.e. a vector with length 1
# We also return the original length, before normalisation.
# We check for zero length, as trying to normalise a zero-length vector results in an error
def safe_normalise(vec):
    length = vec.length()
    if length == 0:
        return Vector2(0,0), 0
    else:
        return vec.normalize(), length

# The MyActor class extends Pygame Zero's Actor class by providing the attribute 'vpos', which stores the object's
# current position using Pygame's Vector2 class. All code should change or read the position via vpos, as opposed to
# Actor's x/y or pos attributes. When the object is drawn, we set self.pos (equivalent to setting both self.x and
# self.y) based on vpos, but taking scrolling into account.
class MyActor(Actor):
    def __init__(self, img, x=0, y=0, anchor=None):
        super().__init__(img, (0, 0), anchor=anchor)
        self.vpos = Vector2(x, y)

    # We draw with the supplied offset to enable scrolling
    def draw(self, offset_x, offset_y):
        # Set Actor's screen pos
        self.pos = (self.vpos.x - offset_x, self.vpos.y - offset_y)
        super().draw()

# Ball physics model parameters
KICK_STRENGTH = 11.5
DRAG = 0.98

# ball physics for one axis
def ball_physics(pos, vel, bounds):
    # Add velocity to position
    pos += vel

    # Check if ball is out of bounds, and bounce if so
    if pos < bounds[0] or pos > bounds[1]:
        pos, vel = pos - vel, -vel

    # Return new position and velocity, applying drag
    return pos, vel * DRAG

# Work out number of physics steps for ball to travel given distance
def steps(distance):
    # Initialize step count and initial velocity
    steps, vel = 0, KICK_STRENGTH

    # Run physics until distance reached or ball is nearly stopped
    while distance > 0 and vel > 0.25:
        distance, steps, vel = distance - vel, steps + 1, vel * DRAG

    return steps

class Goal(MyActor):
    def __init__(self, team):
        x = HALF_LEVEL_W
        y = 0 if team == 0 else LEVEL_H
        super().__init__("goal" + str(team), x, y)

        self.team = team

    def active(self):
        # Is ball within 500 pixels on the Y axis?
        return abs(game.ball.vpos.y - self.vpos.y) < 500

# Calculate if player 'target' is a good target for a pass from player 'source'
# target can also be a goal
def targetable(target, source):
    # Find normalised (unit) vector v0 and distance d0 from source to target
    v0, d0 = safe_normalise(target.vpos - source.vpos)

    # If source player is on a computer-controlled team, avoid passes which are likely to be intercepted
    # (If source is player-controlled, that's the player's job)
    if not game.teams[source.team].human():
        # For each player p
        for p in game.players:
            # Find normalised vector v1 and distance d1 from source to p
            v1, d1 = safe_normalise(p.vpos - source.vpos)