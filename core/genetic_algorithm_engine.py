import random

from core.population_initializer import initialize_population
from strategies.fitness_evaluation_strategies.fitness_evaluation_strategy import fitness_evaluation_strategy
from .individual import Individual



class GeneticAlgorithEngine:

    def __init__(self, population_size, num_generations, grid_size, start, end):
        self.population_size = population_size
        self.num_generations = num_generations
        self.grid_size = grid_size
        self.start = start
        self.end = end


        self.population = []


    def evaluate_indivual(self,individual):

        return fitness_evaluation_strategy(individual.path, self.start, self.end)



    def initialize_population(self):
        paths = initialize_population(self.population_size, self.grid_size)
        for path in paths:
            individual = Individual(path)
            individual.fitness = self.evaluate_indivual(individual=path)

            self.population.append(individual)



    


    def run(self):
        self.initialize_population()
        

        
        for i in range(self.population_size - 1):
            print("Aqui esta el Path")
            print(self.population[i].printPath)
            print("Aqui esta el Fitness")
            print(self.population[i].fitness)
            
           



        #Evaluar el fitness de cada individuo



