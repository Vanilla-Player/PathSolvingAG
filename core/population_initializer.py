
import random

from core.individual import Individual


def initialize_population(population_size, grid_size):
    population = []
    path_length = grid_size[0]*grid_size[1]

    for _ in range(population_size):
        path = generate_random_path(grid_size,path_length)
        individual = Individual(path)
        population.append(individual)


    return population


def generate_random_path(grid_size,path_length):
    path = []

    for _ in range(random.randint(0,path_length)):
        x = random.randint(0, grid_size[0] - 1)
        y = random.randint(0, grid_size[1] - 1)
        path.append((x,y))

    return path