"""Module that alculates the value of the integral of a function using the Monte Carlo method."""

import numpy as np
from scipy.integrate import quad


def f(x):
    """Function to integrate"""
    return x**2


# Define integration bounds
a = 0  # Lower bound
b = 2  # Upper bound

# Define the number of random points to sample
num_points = 1000000

# Generate random x and y coordinates within the integration bounds
x_random = np.random.uniform(a, b, num_points)
y_random = np.random.uniform(0, f(b), num_points)

# Calculate the fraction of points that fall under the curve
num_points_under_curve = np.sum(y_random <= f(x_random))

# Calculate the area of the rectangle containing the curve
area_rectangle = (b - a) * f(b)

# Estimate the area under the curve using Monte Carlo method
area_under_curve = area_rectangle * (num_points_under_curve / num_points)

print("Estimated area under the curve using Monte Carlo method:", area_under_curve)


# Calculate the integral analytically
integral_analytical, _ = quad(f, a, b)

print("Analytical integral value:", integral_analytical)
