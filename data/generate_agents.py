import json
import os
import networkx as nx

def generate_agents(n=100, opinions=7):
    res = []

    b = int(n / opinions)
    current = 0
    op = 0
    for i in range(n):
        agent = {"name": f"a{i}", "status": op}
        current = current + 1

        if current >= b:
            op += 1
            current = 0

        res.append(agent)

    return res


def generate_unbalanced_agents(g=nx.Graph(),):
    res = []

    for i in g.nodes(data=True):
        agent = {"name": f"a{i[0]}"}

        if i[1]['class'] == 'red':
            agent['status'] = 6
            agent["llm_name"] = "llama3.1"
        else:
            agent['status'] = 0
            agent["llm_name"] = "llama3.1"

        res.append(agent)

    return res


if __name__ == "__main__":
    input_folder = "/home/cau/mydata/LLM_OD_Llama3.1/data/balanced"
    output_folder = "/home/cau/mydata/LLM_OD_Llama3.1/sample_data/reverse"

    for h_val in ['0.0', '0.5', '0.25', '0.75', '1.0']:
        graphml_path = os.path.join(input_folder, f"PAH-min0.5-h{h_val}.graphml")
        if not os.path.exists(graphml_path):
            print(f"File not found: {graphml_path}")
            continue
        g = nx.read_graphml(graphml_path)

        agents = generate_unbalanced_agents(g=g)
        
        output_path = os.path.join(output_folder, f"reverse_agents_PAH-min0.5-h{h_val}_100_llama3.json")
        with open(output_path, "w") as f:
            json.dump(agents, f)

