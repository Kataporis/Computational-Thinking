# Project: Exam 2 #3
# Name: Adrian Sandoval-Gonzalez
# Professor: Ralph Hooper
# Class: COSC-3302 Computational Thinking
# Date: 12/3/2023
# Description: This program simulates the "three doors game". It keeps track of how many times contestans would win when staying on the initial door
# vs. switching after one has been eliminated. The goal is approximate the probabilities of each.
import random

def simulate_door_game(n_simulations):
    stay_prize_count = 0
    switch_prize_count = 0
    prize_door = 1

    # Simulate door game scenario
    for simulation in range(n_simulations):
        # Roll a random prize door
        prize_door = random.randint(1, 3)
        # Roll the contestant's initial door
        init_door = random.randint(1, 3)

        # Get the remaining doors
        remaining_doors = [door for door in range(1, 4) if door != init_door and door != prize_door]

        # Open (eliminate) one of the remaining doors
        open_door = random.choice(remaining_doors)

        # Switch choice
        switched_door = next(door for door in range(1, 4) if door != init_door and door != open_door)

        # Roll the door choices
        door_picks = random.sample(range(3), 2)

        # Count the number of wins for each strategy
        if init_door == prize_door:            
            stay_prize_count += 1
        elif switched_door == prize_door:
            switch_prize_count += 1

    # Calculate probabilities
    stay_probability = stay_prize_count / n_simulations
    switch_probability = switch_prize_count / n_simulations

    return stay_prize_count, switch_prize_count, stay_probability, switch_probability

n_simulations = 100000

stay_count, switch_count, stay_probability, switch_probability = simulate_door_game(n_simulations)
print(f"When the contestant chose to stay with their initial pick, they were successful {stay_count} times out of {n_simulations}")
print(f"The probability when staying on the initial door is: {stay_probability:.6f}")
print(f"When the contestant chose to switch their initial pick, they were successful {switch_count} times out of {n_simulations}")
print(f"The probability when switching doors is: {switch_probability:.6f}")