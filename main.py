from core.genetic_algorithm_engine import GeneticAlgorithEngine


population_size = 50

num_generations = 20

grid_size= (3,3)

start = (0,0)

end = (3,3)

ga_engine = GeneticAlgorithEngine(population_size, num_generations, grid_size,start, end)


ga_engine.run()