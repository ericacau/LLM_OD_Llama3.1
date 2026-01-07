from llm_network.simulator import LLMOpinionSimulator
import llm_network as llmn
import networkx as nx
import json
import sys
import os


def execute(
    models,
    config_list,
    network,
    n,
    name,
    theme=None,
    theme_name="theseus_opinion_distr",
    experiment="unbalanced",
    n_agents=100,
    folder=''
):
    llm_config = {
        "config_list": None,
        "seed": 42,
        "max_tokens": 8192,
        "temperature": 0.8,
    }

    # Create a network of agents from files
    net = llmn.Network()
    min_part = experiment.split('-')[1] 
    data_folder = f"min{min_part.split('min')[1].replace('.', '')}" 
    model_name = models.replace(":", "")
    agent_file = f"sample_data/agents_{experiment}_{n_agents}_{model_name}.json"
    print(agent_file)
    net.add_agents(agent_file)

    if network is not None:
        network = network.strip()
        network_path = f"data/{data_folder}/{network}"
        g = nx.read_edgelist(network_path, nodetype=str, delimiter=",")
        g = nx.relabel_nodes(g, lambda x: x.strip())
        net.set_network(g)

    # Load instructions and opinion map
    instructions = json.load(open(f"sample_data/agents_instructions_{theme_name}.json"))
    opinion_map = json.load(open("sample_data/opinion_map.json"))


    # run the simulation
    sim = LLMOpinionSimulator(
        llm_config,
        config_list,
        verbose=False,
        save_agents_debates=True,
        monitor_type="MonitorOpinionDistribution", 
        agents_instruction=instructions,
        opinion_map=opinion_map,
        min_opinion=0,
        max_opinion=6,
    )
    sim.set_agents(net)
    
    os.makedirs("results", exist_ok=True)
    sim.run(
        n_iterations=100,
        themes=theme,
        output_file=f"results/{theme_name}_{name.split('.')[0]}_{model_name}_{n}_{experiment}.jsonl",
    )


if __name__ == "__main__":
    # Simple example
    models = sys.argv[1]
    run_n = int(sys.argv[2])
    theme_name = sys.argv[3]
    exp_name = sys.argv[4]
    n_agents = int(sys.argv[5])
    try:
        network = sys.argv[6]
    except IndexError:
        network = None

    model_list = models.split(",")
    config_list = {}

    # Create a configuration for each model
    for model in model_list:
        config_list[model] = {
            "model": f"{model}",
            "base_url": "http://localhost:11434/v1",
            "api_type": "openai",
            "api_key": "NULL",
            "price": [0, 0],
        }

    #identify current path for different minority classes
    min_part = exp_name.split('-')[1] 
    folder = f"min{min_part.split('min')[1].replace('.', '')}"  

    theme = json.load(open(f"themes/{theme_name}", "r"))

    for n in range(run_n):
        execute(
            models=models,
            config_list=config_list,
            network=network,
            n=n,
            name=theme_name,
            theme=theme,
            experiment=exp_name,
            n_agents=n_agents,
            folder=folder
        )