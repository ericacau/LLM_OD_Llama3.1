import os
import matplotlib as mpl
import json
from collections import defaultdict
import numpy as np
from matplotlib import cm

if os.environ.get("DISPLAY", "") == "":
    print("no display found. Using non-interactive Agg backend")
    mpl.use("Agg")
import matplotlib.pyplot as plt
plt.rc('xtick',labelsize=14)
plt.rc('ytick',labelsize=14)

__author__ = "Giulio Rossetti"
__license__ = "BSD-2-Clause"
__email__ = "giulio.rossetti@gmail.com"


class OpinionArea(object):
    def __init__(self, filename: object):
        """
        :param model: The model object
        :param trends: The computed simulation trends
        """

        self.data = defaultdict(list)

        with open(filename) as file:
            old_iter = 0
            statuses = {}

            print(filename)

            for id_row, l in enumerate(file):
                try:
                    l = json.loads(l)
                    # try:

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

        for k, v in self.data.items():
            self.data[k] = [x / len(l["status"]) for x in self.data[k]]

    def plot(self, filename=None, limit=None, legend=True):
        """
        Generates the plot

        :param filename: Output filename
        :param percentile: The percentile for the trend variance area
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
        categories = [0, 1, 2, 3, 4, 5, 6]
        data = [self.data[k][:limit] if limit else self.data[k] for k in categories]
        x = range(0, len(data[0]))

        # Map numbers to a diverging color palette
        colors = cm.coolwarm(np.linspace(0, 1, len(categories)))

        plt.stackplot(x, data, labels=[label[k] for k in categories], colors=colors, alpha=0.7)

        plt.xlabel("Iterations", fontsize=14)
        plt.ylabel("% Agents", fontsize=14)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.xlim(0,100)
        plt.ylim(0,1)
        if legend:
            plt.legend(loc="best", fontsize=9, ncol=4, bbox_to_anchor=(1.01, 1.18))

        plt.tight_layout()
        if filename is not None:
            plt.savefig(filename)
            plt.clf()
        else:
            plt.show()
