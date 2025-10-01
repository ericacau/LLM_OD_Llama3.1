import os
import matplotlib.pyplot as plt
from llm_network.viz.shift_plot import ShiftMatrix

h_values = ['0.0', '0.25', '0.5', '0.75', '1.0']
min_values = ['0.1', '0.3', '0.5']

# Output directory
os.makedirs("trends/shift_matrices", exist_ok=True)

for min_val in min_values:
    print(f"\nProcessing min_val = {min_val}")
    fig, axes = plt.subplots(1, len(h_values), figsize=(18, 5), sharey=True)

    for idx, h_val in enumerate(h_values):
        min_folder = f"min{min_val.replace('.', '')}"
        # Adapt the filename to your actual shift matrix file naming convention
        shift_filename = f"results/{min_folder}/reverse_theseus_opinion_distr_theseus_same_llama3.1_0_PAH-min{min_val}-h{h_val}.jsonl"
        if os.path.exists(shift_filename):
            sm = ShiftMatrix(shift_filename)

            sm.plot(ax=axes[idx], d="accept")
            axes[idx].set_title(f"h={h_val}", fontsize=14)
        else:
            print(f"File not found: {shift_filename}")
            axes[idx].text(0.5, 0.5, 'No data', ha='center', va='center')

    fig.suptitle(f"Shift Matrix (accept) for min_val={min_val}", fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    output_file = f"trends/shift_matrices/shift_accept_min{min_val}.png"
    plt.savefig(output_file, bbox_inches='tight', dpi=300)
    plt.close(fig)