from llm_network.viz import OpinionTrends, StackedAreaChart
import os.path
import matplotlib.pyplot as plt

h = ['0.0', '0.25', '0.5', '0.75', '1.0']

# Create a figure and axes for subplots
fig, axes = plt.subplots(1, len(h), figsize=(18 , 5), sharey=True)  

min_values = ['0.1', '0.3', '0.5']

for min_val in min_values:
    fig, axes = plt.subplots(1, len(h), figsize=(18, 5), sharey=True)
    for idx, h_val in enumerate(h):
        trends_filename = f"results/reverse/reverse_theseus_theseus_same_llama3.1_0_PAH-min{min_val}-h{h_val}.jsonl"
        if os.path.exists(trends_filename):
            trends_img = StackedAreaChart(trends_filename)
            axfigure = trends_img.plot_no_whitespace(ax=axes[idx])
            axes[idx].set_title(f"h={h_val}", fontsize=14)
            axes[idx].tick_params(axis='x', labelsize=14) 
            axes[idx].tick_params(axis='y', labelsize=14) 
            axes[idx].relim()
            axes[idx].autoscale_view()
            if idx == 0: 
                axes[idx].set_ylabel("% Agents", fontsize=16)

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.05),
               ncol=7, fontsize=14)
    for ax in axes:
        ax.legend().remove()

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(f"trends/opinion_trend/reverse_area_chart_combined_trends_llama3_min{min_val}.png", bbox_inches='tight', dpi=300)
    plt.close(fig)
