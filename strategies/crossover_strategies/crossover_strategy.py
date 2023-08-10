import random

##Esto deberia ser una clase, que herede de la crossover_strategy

def ordered_crossover(parent1,parent2):
    smaller_length = min(len(parent1), len(parent2))
    crossover_point = random.randint(0, smaller_length - 1)
    
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    
    return offspring1, offspring2