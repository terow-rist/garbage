import numpy as np
import math
# Define the function
# def f(x):
#     return 3 * x - math.cos(x) - 1
def f(x):
    return 2*x-math.cos(x)-3

# Find initial guess by searching for a sign change
def find_initial_guess(x_start, x_end, step):
    x_values = np.arange(x_start, x_end, step)
    for i in range(len(x_values) - 1):
        if f(x_values[i]) * f(x_values[i + 1]) < 0:  # Sign change detected
            return (x_values[i] + x_values[i + 1]) / 2  # Midpoint as guess
    return None  # No sign change found

# Search range and step size
x_start, x_end, step = 0, 1, 0.01

# Find the initial guess
initial_guess = find_initial_guess(x_start, x_end, step)
print(initial_guess)
