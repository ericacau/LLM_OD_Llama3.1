import numpy as np
import json 
import os
import networkx as nx
from tqdm import tqdm
from statistical_validation.NullModels import LODSNullModel


def load_graph(minority_size, h, base_path='data/graphs/'):
    """
    Load a graph based on the minority size.
    This function creates a random graph with a specified number of nodes and edges.
    """
    # read graphml file
    # ex path: PAH-min0.1-h0.0.graphml
    path = f'{base_path}PAH-min{minority_size}-h{h}.graphml'
    if not os.path.exists(path):
        raise FileNotFoundError(f"Graph file not found: {path}")
    G = nx.read_graphml(path, node_type=int)

    return G
                
nruns = 10
niter = 30
opinion_space = list(range(7))
minority_sizes = [0.1, 0.3, 0.5]
homophily_rates = [0.0, 0.25, 0.5, 0.75, 1.0]
rules = ['random', 'always_accept', 'always_reject', 'biased_upward']



# Main loop with tqdm
with tqdm(total=len(minority_sizes) * len(homophily_rates) * nruns * len(rules)) as pbar:
    
    for min_size in minority_sizes:
        for h in homophily_rates:
            base_path = f'statistical_validation/results/{min_size}/{h}'
            os.makedirs(base_path, exist_ok=True)
            g = load_graph(min_size, h)
            for rule in rules:    
                            
                for run in range(nruns):
                    
                    model = LODSNullModel(g, min_size, opinion_space, rule)
                    iterations = model.iteration_bunch(niter)
                    
                    run_transition_matrix = np.zeros((len(opinion_space), len(opinion_space)))
                    evolution = {k: [] for k in opinion_space}

                    for res in iterations:
                        status = res['status']

                        # Count how many nodes have each opinion
                        opinion_counts = np.zeros(len(opinion_space))
                        for opinion in status.values():
                            opinion_counts[opinion] += 1
                        for opinion, count in enumerate(opinion_counts):
                            evolution[opinion].append(count)

                        # Process opinion transitions
                        transitions = res.get('transitions', [])
                        for from_op, to_op in transitions:
                            run_transition_matrix[from_op, to_op] += 1

                        
                    np.save(f'{base_path}/transition_matrix_{rule}_{run}.npy', run_transition_matrix)
                    with open(f'{base_path}/evolution_{rule}_{run}.json', 'w') as f:
                        json.dump(evolution, f)

                    pbar.update(1)



                
                
                

                

                

            

