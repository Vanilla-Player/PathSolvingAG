

def fitness_evaluation_strategy(path,start,end):

    total_STEPS = 0
    fitness = 0

    for i in range(len(path) - 1):
        current_node = path[i]

        next_node = path[i + 1]

        #Not valid Path Ex : (0,0) -> (2,2)! exclude 
        if(abs(next_node[0] - current_node[0]) > 1 or abs(next_node[1] - current_node[1]) > 1):
            fitness = 0
            return fitness
        
        total_STEPS += 1
    
    
    
    # Add a penalty for paths that do not start or end at desired points
        
    if path[0] != start or path[-1] != end:
        total_STEPS += 100000

    
    fitness = 1 / total_STEPS

    return fitness



