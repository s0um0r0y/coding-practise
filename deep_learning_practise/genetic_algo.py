import numpy as np

# defines a fitness function
def fitness_function(individual):
    return -np.sum(individual**2)

# generate an initial poplulation
def generate_population(size, dim):
    return np.random.rand(size, dim)

# genectic algorithm
def genetic_algorithm(population, fitness_func, n_generation=100, mutation_rate=0.01):
    for _ in range(n_generation):
        population = sorted(population, key=fitness_func, reverse=True)
        next_generation = population[:len(population)//2].copy()
        while len(next_generation) < len(population):
            parents_indices = np.random.choice(len(next_generation), 2, replace=False)
            parent1, parent2 = next_generation[parents_indices[0]], next_generation[parents_indices[1]]
            crossover_point = np.random.randint(1, len(parent1))
            child = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
            if np.random.rand() < mutation_rate:
                mutate_point = np.random.randint(len(child))
                child[mutate_point] = np.random.rand()
            next_generation.append(child)
            population = np.array(next_generation)
        return population[0]
    
# Parameters
population_size = 10
dimension = 5
n_generations = 50
mutation_rate = 0.05

# initialize population
population = generate_population(population_size, dimension)

# run genetic algorithm
best_individual = genetic_algorithm(population, fitness_function, n_generations, mutation_rate)

# Output the best individual and its fitness
print("Best individual:", best_individual)
print("Best fitness:", -fitness_function(best_individual))