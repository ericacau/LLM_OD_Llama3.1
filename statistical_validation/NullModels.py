import random
from tqdm import tqdm
import networkx as nx

class LODSNullModel(object):
    """
    Class for the networked LODS null model.
    """

    def __init__(self,
                 G: nx.Graph,
                 minority_size: list,
                 opinion_space: list,
                 rule: str = 'random',
                 ):

        self.N = G.number_of_nodes()
        self.G = G
        self.minority_size = minority_size
        self.opinion_space = opinion_space
        self.rule = rule
        self.t = 0  # Initialize time step
        self.status = dict()
        
        probabilities = [1 - self.minority_size, self.minority_size, ]

        opinions = random.choices([0, 6], probabilities, k=self.N)
        self.status = dict(zip(range(self.N), opinions))

    def opinion_update(self, opinion_i, opinion_j):
        """
        Update the opinion of node i based on the opinion of node j.
        The update rule depends on the model's rule.
        """
        if self.rule == 'random':
            return random.choice([-1, 0, 1])
        elif self.rule == 'always_accept':
            return 1 if opinion_j > opinion_i else -1
        elif self.rule == 'always_reject':
            return -1 if opinion_j > opinion_i else 1
        elif self.rule == 'biased_upward':
            return 1 if opinion_j > opinion_i else 0

        else:
            raise ValueError(f"Unknown rule: {self.rule}")
    
    def is_possible(self, opinion, change):
        return opinion + change in self.opinion_space
    

    def iteration(self):
        # Copy current status to work with
        current_status = self.status.copy()
        transitions = []

        # Iterate over all pairs of nodes
        for i in self.G.nodes():
            neighs = list(self.G.neighbors(i))
            if not neighs:
                continue
            j = random.choice(neighs)
        

            change = self.opinion_update(current_status[i], current_status[j])

            if self.is_possible(current_status[i], change):
                old = current_status[i]
                new = old + change
                current_status[i] = new
                transitions.append((old, new))

        # Update the model's state
        self.status = current_status

        # Return the state and transitions for this iteration
        return {
            'iteration': self.t,
            'status': current_status.copy(),
            'transitions': transitions
        }

    def iteration_bunch(self, bunch_size):
        iterations = []
        # Store the initial state
        iterations.append({
            'iteration': 0,
            'status': self.status.copy(),
            'transitions': []
        })

        for t in range(1, bunch_size):
            self.t = t
            result = self.iteration()
            iterations.append(result)
            
        return iterations


