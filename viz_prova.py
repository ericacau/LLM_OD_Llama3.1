from llm_network.viz import OpinionTrends, ShiftMatrix
import os.path

h = ['0.0', '0.5', '0.25', '0.75', '1.0']

for h_val in h:
    # Plot OpinionTrends
    trends_filename = f"results/theseus_theseus_same_llama3.1_0_PAH-min0.3-h{h_val}.jsonl"
    if os.path.exists(trends_filename):
        trends_img = ShiftMatrix(trends_filename)
        trends_img.plot(f"trends/theseus_matrix_same_llama3.1_0_PAH-min0.3-h{h_val}.png")
