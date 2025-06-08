import math
import random
import matplotlib.pyplot as plt

missileCo = (random.randint(-10, -1), random.randint(-10, -1))
planeCo = (10, 10)

class Missile():
    def __init__(self):
        self.missile_id = None
        self.difX = 0
        self.difY = 0
        self.distance = 0

    def measureDis(self, missileCo, planeCo):
        mx, px = missileCo[0], planeCo[0]
        my, py = missileCo[1], planeCo[1]

        self.difX = mx - px
        self.difY = my - py

        distanceSq = (self.difY * self.difY) + (self.difX * self.difX)

        self.distance = math.sqrt(distanceSq)
        print (f"Adj: {-1 *self.difY}")
        print (f"Opp: {-1 *self.difX}")
        return self.distance

    def measureAng(self):
        if self.difY != 0:
            tanangle = self.difX / self.difY
            angle = math.degrees(math.atan(tanangle))
            return angle
        else:
            return None

missile = Missile()

# Prepare the plot
plt.figure(figsize=(10, 10))
plt.scatter(*planeCo, color='red', label='Plane')
plt.xlim(-15, 15)
plt.ylim(-15, 15)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

for i in range(1000):
    missileCo = (random.randint(1, 10), random.randint(1, 10))
    print(f"Xco: {missileCo[0]}")
    print(f"Yco: {missileCo[1]}")
    print(f"Hyp: {missile.measureDis(missileCo, planeCo)}")
    print(f"Ang: {missile.measureAng()}")
    print("\n")
    
    # Plot the missile coordinates
    plt.scatter(*missileCo, color='blue', alpha=0.5)
    plt.pause(0.01)  # Pause to update the plot

# Add labels and legend
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Missile and Plane Coordinates')
plt.legend()

# Show the plot
plt.show()
