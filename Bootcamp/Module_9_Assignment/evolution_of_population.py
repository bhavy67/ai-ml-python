# Library
import random

# Global seed value for reproducibility
GLOBAL_SEED = 42
random.seed(GLOBAL_SEED)

# Lowercase letters (a to z)
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

# Function to generate a random code (string of 10 characters)
def generate_random_code():
    return ''.join(random.choice(LOWERCASE_LETTERS) for _ in range(10))

# Function to calculate fitness (number of characters matching the target code)
def calculate_fitness(code, target_code):
    return sum(1 for c1, c2 in zip(code, target_code) if c1 == c2)

# Function to apply mutation to a code with a probability of 0.1
def mutate(code):
    if random.random() < 0.1:
        idx = random.randint(0, 9)  # choose a random index
        new_char = random.choice(LOWERCASE_LETTERS)  # random new character
        code = code[:idx] + new_char + code[idx + 1:]  # replace character at index
    return code

# Function to perform crossover between two codes
def crossover(parent1, parent2):
    point = random.randint(1, 9)  # random crossover point
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

# Function to calculate the mean and standard deviation of a list of numbers
def calculate_mean_and_std_dev(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = variance ** 0.5
    return round(mean, 2), round(std_dev, 2)

# Main function to simulate the genetic algorithm
def evolve_population_to_target(target_code):
    population_size = 100
    population = [generate_random_code() for _ in range(population_size)]
    generations = 0
    fitness_history = []

    while generations < 100:
        generations += 1

        # Calculate fitness for each code in the population
        fitness_scores = [calculate_fitness(code, target_code) for code in population]

        # Check if any code has perfectly matched the target and terminate loop
        if max(fitness_scores) == 10:
            break

        # Collect statistics for this generation
        fitness_mean, fitness_std_dev = calculate_mean_and_std_dev(fitness_scores)
        fitness_history.append((fitness_mean, fitness_std_dev))

        # Select the top 50% of the population based on fitness
        selected_population = [population[i] for i in range(population_size) if fitness_scores[i] >= sum(fitness_scores) / len(fitness_scores)]

        # Reproduce the next generation
        next_population = []
        while len(next_population) < population_size:
            parent1, parent2 = random.sample(selected_population, 2)  # select two random parents
            offspring1, offspring2 = crossover(parent1, parent2)  # perform crossover
            next_population.extend([mutate(offspring1), mutate(offspring2)])  # apply mutation

        population = next_population[:population_size]  # keep the population size constant

    # Prepare final statistics
    fitness_mean, fitness_std_dev = fitness_history[-1]
    return {
        'generations': generations,
        'fitness_stats': {'mean': fitness_mean, 'std_dev': fitness_std_dev},
    }

# Input and output processing
print(evolve_population_to_target(input()))