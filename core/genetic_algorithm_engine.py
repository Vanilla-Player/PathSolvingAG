import random

from core.population_initializer import initialize_population



class GeneticAlgorithEngine:

    def __init__(self, population_size, num_generations, grid_size):
        self.population_size = population_size
        self.num_generations = num_generations
        self.grid_size = grid_size



        self.population = []


    def initialize_population(self):
        population = initialize_population(self.population_size, self.grid_size)

    def run(self):
        self.initialize_population()
        #Evaluar el fitness de cada individuo



