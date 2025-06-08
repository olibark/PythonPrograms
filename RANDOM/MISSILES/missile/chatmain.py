import math
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# plane coordinates (fixed)
planeCo = (10, 10)

fig, ax = plt.subplots()
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_aspect('equal')
ax.set_title("Missile and Plane Triangle Animation")

# Lines for hypotenuse, adjacent, and opposite sides
hyp_line, = ax.plot([], [], 'r-', lw=2, label="Hypotenuse", animated=True)
adj_line, = ax.plot([], [], 'g--', lw=2, label="Adjacent", animated=True)
opp_line, = ax.plot([], [], 'b--', lw=2, label="Opposite", animated=True)

# Plot the fixed plane point and add its label
plane_point, = ax.plot(planeCo[0], planeCo[1], 'bo')
plane_label = ax.text(planeCo[0] + 0.5, planeCo[1] + 0.5, "Plane", fontsize=12, color="blue")

# Create the missile point and label (initially empty) and mark them as animated
missile_point, = ax.plot([], [], 'ro', animated=True)
missile_label = ax.text(0, 0, "", animated=True, fontsize=12, color="red")

ax.legend()

def init():
    hyp_line.set_data([], [])
    adj_line.set_data([], [])
    opp_line.set_data([], [])
    missile_point.set_data([], [])
    missile_label.set_text("")
    return hyp_line, adj_line, opp_line, missile_point, missile_label

def animate(frame):
    # Update missileCo randomly
    missileCo = (random.randint(1, 10), random.randint(1, 10))
    
    # Hypotenuse: line from plane to missile
    hyp_line.set_data([planeCo[0], missileCo[0]], [planeCo[1], missileCo[1]])
    
    # Opposite side: vertical line from missile to plane's y-coordinate
    opp_line.set_data([missileCo[0], missileCo[0]], [missileCo[1], planeCo[1]])
    
    # Adjacent side: horizontal line from missile to plane's x-coordinate
    adj_line.set_data([missileCo[0], planeCo[0]], [planeCo[1], planeCo[1]])
    
    # Update the missile point and its label
    missile_point.set_data(missileCo[0], missileCo[1])
    missile_label.set_position((missileCo[0] + 0.5, missileCo[1] + 0.5))
    missile_label.set_text("Missile")
    
    ax.set_title(f"Missile: {missileCo}")
    return hyp_line, adj_line, opp_line, missile_point, missile_label

ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init, interval=500, blit=True)
plt.show()