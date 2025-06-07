import pygame
import random
import sys

# Window dimensions
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

# Number of particles
NUM_PARTICLES = 50

class Particle:
    def __init__(self):
        # Random initial position
        self.x = random.uniform(0, WINDOW_WIDTH)
        self.y = random.uniform(0, WINDOW_HEIGHT)
        # Random velocity between -5 and 5
        self.vx = random.uniform(-5, 5)
        self.vy = random.uniform(-5, 5)
        # Particle size (radius)
        self.size = random.randint(5, 10)
        # Random colour
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    def update(self):
        # Update position
        self.x += self.vx
        self.y += self.vy
        self.vx = (self.vx -1) * 0.5
        self.vx = (self.vx -1) * 0.5

        # Bounce off left or right edges
        if self.x < 0:
            self.x = 0
            self.vx = -self.vx
            self.vx = (self.vx -1) * 0.5
            self.vx = (self.vx -1) * 0.5
        elif self.x > WINDOW_WIDTH - self.size:
            self.x = WINDOW_WIDTH - self.size
            self.vx = -self.vx
            self.vx = (self.vx -1) * 0.5
            self.vx = (self.vx -1) * 0.5
        # Bounce off top or bottom edges
        if self.y < 0:
            self.y = 0
            self.vy = -self.vy
            self.vx = (self.vx -1) * 0.5
            self.vx = (self.vx -1) * 0.5
        elif self.y > WINDOW_HEIGHT - self.size:
            self.y = WINDOW_HEIGHT - self.size
            self.vy = -self.vy
            self.vx = (self.vx -1) * 0.5
            self.vx = (self.vx -1) * 0.5
    def draw(self, surface):
        # Draw particle as a filled circle
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

def main():
    # Initialise Pygame
    pygame.init()

    # Create a window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Bouncing Particles")

    # Create a clock to control the frame rate
    clock = pygame.time.Clock()

    # Create a list of particles
    particles = [Particle() for _ in range(NUM_PARTICLES)]

    # Main loop
    running = True
    while running:
        # Limit the frame rate (60 FPS)
        clock.tick(6000)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Update all particles
        for particle in particles:
            particle.update()

        # Clear screen (fill with black)
        screen.fill((0, 0, 0))

        # Draw all particles
        for particle in particles:
            particle.draw(screen)

        # Flip the display buffer
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
