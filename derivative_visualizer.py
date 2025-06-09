import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sympy import symbols, sympify, diff


def main():
    expr_str = input("Enter a function of x (e.g. x**2 + 3*x): ")
    x_val_str = input("Enter x value to show tangent/normal: ")

    try:
        x_val = float(x_val_str)
    except ValueError:
        print("Invalid x value")
        return

    x = symbols('x')
    try:
        expr = sympify(expr_str)
    except Exception as e:
        print(f"Invalid expression: {e}")
        return

    deriv = diff(expr, x)
    f = lambda t: np.array([expr.subs(x, t).evalf()], dtype=float)[0]
    df = lambda t: np.array([deriv.subs(x, t).evalf()], dtype=float)[0]

    x_range = np.linspace(x_val - 10, x_val + 10, 400)
    y_vals = [f(t) for t in x_range]

    fig, ax = plt.subplots()
    ax.set_xlim(x_range.min(), x_range.max())
    ax.set_ylim(min(y_vals) - 5, max(y_vals) + 5)
    ax.plot(x_range, y_vals, label='f(x)')
    point, = ax.plot([], [], 'ro')
    tan_line, = ax.plot([], [], 'g--', label='Tangent')

    slope_at_x0 = df(x_val)
    intercept = f(x_val) - slope_at_x0 * x_val
    normal_slope = -1 / slope_at_x0 if slope_at_x0 != 0 else np.inf
    normal_intercept = f(x_val) - normal_slope * x_val
    print(f"Tangent line at x={x_val}: y = {slope_at_x0:.3f}x + {intercept:.3f}")
    if normal_slope != np.inf:
        print(f"Normal line at x={x_val}: y = {normal_slope:.3f}x + {normal_intercept:.3f}")
    else:
        print("Normal line is vertical")

    def update(frame):
        x_point = x_range[frame]
        y_point = f(x_point)
        point.set_data([x_point], [y_point])
        m = df(x_point)
        b = y_point - m * x_point
        x_tan = np.linspace(x_point - 2, x_point + 2, 10)
        tan_line.set_data(x_tan, m * x_tan + b)
        return point, tan_line

    ani = FuncAnimation(fig, update, frames=len(x_range), interval=20, blit=True, repeat=True)
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()
