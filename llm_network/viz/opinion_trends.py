import os
import matplotlib as mpl
import json
from collections import defaultdict
import numpy as np
from .plot_config import apply_plot_config


if os.environ.get("DISPLAY", "") == "":
    print("no display found. Using non-interactive Agg backend")
    mpl.use("Agg")
import matplotlib.pyplot as plt

__author__ = "Giulio Rossetti"
__license__ = "BSD-2-Clause"
__email__ = "giulio.rossetti@gmail.com"


class OpinionTrends(object):
    def __init__(self, filename: object):
        """
        :param model: The model object
        :param trends: The computed simulation trends
        """

        self.data = defaultdict(list)
        try: 
            with open(filename) as file:
                old_iter = 0
                statuses = {}

                for id_row, l in enumerate(file):
                    try:
                        l = json.loads(l)
                        iter = l["iteration"]
                    except:
                        continue

                    if iter == old_iter:
                        statuses = l["status"]
                    else:
                        sts = {
                            k: sum(value == k for value in statuses.values())
                            for k in range(0, 7)
                        }
                        old_iter = iter
                        for k, v in sts.items():
                            self.data[k].append(v)      
        except:
            print(filename)    

        for k, v in self.data.items():
            self.data[k] = [x / len(l["status"]) for x in self.data[k]]

    def plot(self, ax, filename=None, limit=None):
        """
        Generates the plot

        :param filename: Output filename
        :param limit: Number of iterations showed
        
        """
                
        label = {
            0: "Strongly Disagree",
            1: "Disagree",
            2: "Mildly Disagree",
            3: "Neutral",
            4: "Mildly Agree",
            5: "Agree",
            6: "Strongly Agree",
        }
        for k in [0, 6, 1, 5, 2, 4, 3]:
            if limit is None:
                ax.plot(
                    x = range(0, len(self.data[k])),
                    y = self.data[k],
                    label=label[k],
                )
            else:
                try:
                    y = self.data[k][:limit]
                    ax.plot(
                            [_ for _ in range(0, limit)],
                            y,
                            label=label[k],
                        )
                except ValueError as e:
                    print(e)
                    print(filename)
                    y = self.data[k]
                    ax.plot(
                            range(len(y)),
                            y,
                            label=label[k],
                        )
                    
        # Label the axes
        ax.set_xlabel("Iterations")  # X-axis label
        ax.set_ylabel("%Agents")  # Y-axis label
        ax.set_ylim(-0.01, 1.01)
        
        if filename is None:
            plt.show()
        else:
            plt.savefig(filename, dpi=300, facecolor='white', bbox_inches='tight')
            
            
            