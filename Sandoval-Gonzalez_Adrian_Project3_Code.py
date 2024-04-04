# Project: Project 3 -- Numerical Analysis
# Name: Adrian Sandoval-Gonzalez
# Professor: Ralph Hooper
# Class: COSC-3302 Computational Thinking
# Date: 11/12/2023
# Description: This program will approximate the derivative at two points for one algebraic function, then at another two points
# for a different algebraic function. To do so, a numerical differentiation approach will be employed. Furthermore, a numerical
# integration approach will be used to approximate the area curve for a different algebraic function.
import math


# Part 1 -- Numerical Differentiation

# This function defines the alebraic function f(x)
def f(x):
    return 4*x**3 + 2*x**2 - 3*x + 5

# This function approximates the derivative at a point a by iteratively modifying the h value until the tolerance is satisfied.
# Inputs: Value to approximate derivative at, tolerance, initial h (difference of x values)
# Outputs: Final derivative, final h
def approximate_derivative(a, tolerance, initial_h):
    h = initial_h
    prev_df = None

    while True:
        # Calculate derivative
        df = (f(a + h) - f(a)) / h

        # Break if the current derivative minus the previous derivative is less than the tolerance
        if prev_df is not None and abs(df - prev_df) < tolerance:
            break

        prev_df = df    # Calculated derivative becomes previous derivative
        h /= 2          # Halve the difference of x values (h)

    return df, h

# Approximate the derivative at x = 1
a = 1
tolerance = 0.01   # Choose a value for acceptable error (tolerance)
initial_h = 0.0001     # Choose a value for the initial difference of x values

derivative_at_a, final_h = approximate_derivative(a, tolerance, initial_h)
print(f"The approximate derivative of f(x) at x = {a} is: {round(derivative_at_a)}")
print(f"The final h value (difference in x values) is: {final_h}\n")

# Approximate the derivative at x = -3
a = -3

derivative_at_a,final_h = approximate_derivative(a, tolerance, initial_h)
print(f"The approximate derivative of f(x) at x = {a} is: {round(derivative_at_a)}")
print(f"The final h value (difference in x values) is: {final_h}\n")

# Repeat for the second function
def f(x):
    return x**2 * math.cos(x)

# Approximate at x = 0
a = 0

derivative_at_a, final_h = approximate_derivative(a, tolerance, initial_h)
print(f"The approximate derivative of g(x) at x = {a} is: {round(derivative_at_a)}")
print(f"The final h value (difference in x values) is: {final_h}\n")

# Approximate at x = pi
a = math.pi

derivative_at_a, final_h = approximate_derivative(a, tolerance, initial_h)
print(f"The approximate derivative of g(x) at x = {a} is: {round(derivative_at_a)}")
print(f"The final h value (difference in x values) is: {final_h}\n")

# Part 2 -- Numerical Integration

# This function defines the algebraic function g(x)
def h(x):
    return 0.34*x**2 + 2.98*x + 1.53

# This function sums the areas of the n subintervals to approximate the integral.
# Inputs: Left bound of integral, right bound of integral, number of subintervals
# Outputs: Area beneath the curve
def riemann_sum(a, b, n):
    delta_x = (b - a) / n
    area = 0

    for i in range(n):
        x_i = a + i * delta_x
        area += max(0, h(x_i)) * delta_x  # Ensure the function value is non-negative

    return area

# This function iterates through different numbers of subintervals until the tolerance is satisfied. It calls the riemnann_sum function.
# Inputs: Tolerance, initial number of subintervals
# Outputs: Final area, final number of subintervals
def approximate_area(tol, initial_n):
    n = initial_n
    prev_area = None

    while True:
        current_area = riemann_sum(2, 4, n)

        # Break if the current area - previous area satisfies the tolerance
        if prev_area is not None and abs(current_area - prev_area) < tol:
            break

        prev_area = current_area    # Current area becomes the previous area
        n *= 2                      # Double the number of subintervals

    return current_area, n

# Choose values for tolerance and initial subintervals
tolerance = 0.00001
initial_n = 400000

# Approximate the integral from 2 to 4, storing the number of subintervals as well
result, subintervals = approximate_area(tolerance, initial_n)

print(f"Integral approximation for h(x) from 2 to 4: {result}")
print(f"Number of subintervals: {subintervals}")