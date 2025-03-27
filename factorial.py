# Project: Exam 2 #7
# Professor: Ralph Hooper
# Class: COSC-3302 Computational Thinking
# Date: 12/7/2023
# Description: This program solves a factorial using an iterative approach.
def solve_factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
        return factorial

num = 3
result = solve_factorial(num)
print(f"The factorial of {num} is equal to: {result}")
