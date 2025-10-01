from llm_network.viz import area_chart
import os.path
import matplotlib.pyplot as plt
from collections import defaultdict
from llm_network.viz.area_chart import StackedAreaChart
from llm_network.viz.opinion_volume import OpinionVolume

# Create output directory
os.makedirs("trends/opinion_volume", exist_ok=True)

h_values = ['0.0', '0.25', '0.5', '0.75', '1.0']
min_values = ['0.1', '0.3', '0.5']


for min_val in min_values:
    print(f"\nProcessing min_val = {min_val}")
    fig, axes = plt.subplots(1, len(h_values), figsize=(18, 5), sharey=True)
    
    for idx, h_val in enumerate(h_values):
        min_folder = f"min{min_val.replace('.', '')}"
        trends_filename = f"results/{min_folder}/reverse_theseus_opinion_distr_theseus_same_llama3.1_0_PAH-min{min_val}-h{h_val}.jsonl"
        
        if os.path.exists(trends_filename):
            trends_img = OpinionVolume(trends_filename)
            lines = trends_img.plot(ax=axes[idx], limit=30)
            
            axes[idx].set_title(f"h={h_val}", fontsize=14)
            axes[idx].tick_params(axis='both', labelsize=12)
            
            if idx == 0:
                axes[idx].set_ylabel("% Agents", fontsize=14)
        else:
            print(f"File not found: {trends_filename}")
            axes[idx].text(0.5, 0.5, 'No data', ha='center', va='center')

    # Get handles and labels from first subplot
    handles, labels = axes[0].get_legend_handles_labels()
    
    # Add single legend above all subplots
    if handles:
        fig.legend(handles, labels,
                  loc='upper center',
                  bbox_to_anchor=(0.5, 1.05),
                  ncol=7, fontsize=14)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    output_file = f"trends/opinion_volume/reverse_opinion_volume_llama3_min{min_val}.png"
    plt.savefig(output_file, bbox_inches='tight', dpi=300)
    plt.close(fig)