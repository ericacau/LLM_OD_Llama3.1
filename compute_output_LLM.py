import json
import numpy as np
from itertools import product
import os
from tqdm import tqdm
from collections import Counter, defaultdict

def compute_matrix(resfile, opinion_space, max_iter=30):
    transition_matrix = np.zeros((len(opinion_space), len(opinion_space)))
    iteration_counts = Counter()
    total_transitions = 0

    with open(resfile, encoding='UTF-8') as f:
        for line in f:
            try:
                data = json.loads(line)
                it = data['iteration']
                iteration_counts[it] += 1

                if 0 < it <= max_iter:
                    old_discussant_opinion = data['interacting_agents']['discussant_opinion']
                    new_discussant_opinion = old_discussant_opinion + data['opinion_variation_discussant']

                    transition_matrix[old_discussant_opinion, new_discussant_opinion] += 1
                    total_transitions += 1
                    
            except (KeyError, json.JSONDecodeError) as e:
                print(f"Error reading line: {e}")
                continue

    for it in sorted(iteration_counts):
        if iteration_counts[it] != 140 and 0 < it <= max_iter:
            print(f"\nIteration counts in file {resfile}:")
            print(f"  Iteration {it}: {iteration_counts[it]} lines")

    return transition_matrix


def compute_transitions(outpath='statistical_validation/results'):
    opinion_space = list(range(7))
    minority_sizes = [0.1, 0.3, 0.5]
    homophily_rates = [0.0, 0.25, 0.5, 0.75, 1.0]
    
    max_iter = 30
    nruns = 12

    combos = list(product(minority_sizes, homophily_rates))


    for minority_size, homophily_rate in tqdm(combos, desc="Processing combinations"):
        os.makedirs(f'{outpath}/{minority_size}/{homophily_rate}', exist_ok=True)
        # PAH-min0.1-h0.0.graphml
        graph_name = f'PAH-min{minority_size}-h{homophily_rate}'
        for run in range(nruns):
            resfile = f"results/theseus_theseus_same_llama3.1_0_{graph_name}.jsonl"
            
            run_transition_matrix = compute_matrix(resfile, opinion_space, max_iter)
            np.save(f'{outpath}/{minority_size}/{homophily_rate}/transition_matrix_real.npy', run_transition_matrix)


compute_transitions()
