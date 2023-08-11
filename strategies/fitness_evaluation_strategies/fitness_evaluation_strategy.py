

def fitness_evaluation_strategy(path,start,end):

    total_STEPS = 0
    fitness = 0

    if(path == []):
        return fitness

    for i in range(len(path) - 1):
        current_node = path[i]

        next_node = path[i + 1]

        #Not valid Path Ex : (0,0) -> (2,2)! exclude, so fitness 0 
        if(abs(next_node[0] - current_node[0]) > 1 or abs(next_node[1] - current_node[1]) > 1):
  
            return fitness
        
        total_STEPS += 1
    
    
    
    # Add a penalty for paths that do not start or end at desired points, but still considering them
    
    if path[0] != start:
        total_STEPS += 100

    if path[-1] != end:
        total_STEPS += 100

    
    fitness = 1 / total_STEPS

    return fitness



