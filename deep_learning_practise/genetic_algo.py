import numpy as np

# defines a fitness function
def fitness_function(individual):
    return -np.sum(individual**2)

# generate an initial poplulation
def generate_population(size, dim):
    return np.random.rand(size, dim)

# genectic algorithm
def genetic_algorithm(population, fitness_func, h_generation=100, mutation_rate=0.01):
    