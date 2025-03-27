# Project: Exam 2 #1
# Professor: Ralph Hooper
# Class: COSC-3302 Computational Thinking
# Date: 12/1/2023
# Description: This program approximates the probability that n_dice all come out to the same number.
import random

def simulate_dice_rolls(n_simulations, n_dice):
    same_number_count = 0

    for simulation in range(n_simulations):
        # Simulate rolling n_dice and check if all numbers are the same
        rolls = [random.randint(1, 6) for die in range(n_dice)]
        if all(roll == rolls[0] for roll in rolls):
            same_number_count += 1

    probability = same_number_count / n_simulations
    return same_number_count, probability

# Choose the number of dice and simulations
n_dice = 5
n_simulations = 100000  # Adjust the number of trials for desired accuracy

occurrences, probability = simulate_dice_rolls(n_simulations, n_dice)

print(f"The dice all came out to the same number {occurrences} times out of {n_simulations} simulations.")
print(f"The approximate probability of getting the same number on rolling {n_dice} dice is: {probability:.6f}")
