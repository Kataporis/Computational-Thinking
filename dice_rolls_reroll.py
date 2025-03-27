# Project: Exam 2 #2
# Professor: Ralph Hooper
# Class: COSC-3302 Computational Thinking
# Date: 12/1/2023
# Description: This program approximates the probability of n_dice all coming out to the same number, assuming dice can be re-rolled.
import random

# This function determines the most frequent element in a list
def most_frequent(List):
    # Init variables
	counter = 0
	num = List[0]
	
    # Determine the most frequent element in list
	for element in List:
		curr_frequency = List.count(element)
		if(curr_frequency > counter):
			counter = curr_frequency
			num = element

	return num

def simulate_dice_rolls(n_simulations, n_dice):
    same_number_count = 0

    # Simulate rolling n_dice
    for simulation in range(n_simulations):
        rolls = [random.randint(1, 6) for die in range(n_dice)]

        # Check if 2 or more dice have the same number
        if any(rolls.count(roll) >= 2 for roll in rolls):
            # Find the roll that occurs most often
            most_frequent_roll = most_frequent(rolls)

            # Re-roll the other dice
            for roll in range(n_dice):
                if rolls[roll] != most_frequent_roll:
                    rolls[roll] = random.randint(1, 6)

            # Check if all numbers are now the same
            if all(roll == rolls[0] for roll in rolls):
                same_number_count += 1

    probability = same_number_count / n_simulations
    return same_number_count, probability

# Choose the number of simulations
n_dice = 5
n_simulations = 100000  # Adjust the number of trials for desired accuracy

occurrences, probability = simulate_dice_rolls(n_simulations, n_dice)

print(f"The dice all came out to the same number {occurrences} times out of {n_simulations} simulations.")
print(f"The simulated probability of getting the same number on rolling {n_dice} dice (with re-rolling) is: {probability:.6f}")
