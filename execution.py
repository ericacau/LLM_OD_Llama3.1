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
    theme_name="theseus_opinion_distr_vllm",
    experiment="unbalanced",
    n_agents=100,
    folder='',
    use_vllm=False,
    vllm_url=None,
    vllm_mode="server",
    n_iterations=100,
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

    monitor_type = "MonitorOpinionDistributionVLLM" if use_vllm else "MonitorOpinionDistribution"

    # run the simulation
    sim = LLMOpinionSimulator(
        llm_config,
        config_list,
        verbose=False,
        save_agents_debates=True,
        monitor_type=monitor_type, 
        agents_instruction=instructions,
        opinion_map=opinion_map,
        min_opinion=0,
        max_opinion=6,
        vllm_url=vllm_url,
        vllm_mode=vllm_mode,
    )
    sim.set_agents(net)
    
    os.makedirs("results", exist_ok=True)
    sim.run(
        n_iterations=n_iterations,
        themes=theme,
        output_file=f"results/{theme_name}_{name.split('.')[0]}_{model_name}_{n}_{experiment}.jsonl",
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="LLM Opinion Simulator Execution script")
    parser.add_argument("models", type=str, help="Comma-separated list of models to use")
    parser.add_argument("run_n", type=int, help="Number of runs")
    parser.add_argument("theme_name", type=str, help="Theme JSON file name")
    parser.add_argument("exp_name", type=str, help="Experiment name")
    parser.add_argument("n_agents", type=int, help="Number of agents")
    parser.add_argument("network", type=str, nargs="?", default=None, help="Optional network file path")
    parser.add_argument("--vllm", action="store_true", help="Use batched vLLM backend")
    parser.add_argument("--vllm-url", type=str, default="http://localhost:8000/v1", help="vLLM server API base URL")
    parser.add_argument("--vllm-mode", type=str, default="server", choices=["server", "offline"], help="vLLM batching mode")
    parser.add_argument("-i", "--iterations", type=int, default=100, help="Number of simulation iterations")

    args = parser.parse_args()

    models = args.models
    run_n = args.run_n
    theme_name = args.theme_name
    exp_name = args.exp_name
    n_agents = args.n_agents
    network = args.network

    model_list = models.split(",")
    config_list = {}

    # Create a configuration for each model
    for model in model_list:
        config_list[model] = {
            "model": f"{model}",
            "base_url": "http://localhost:11434/v1",
            "api_type": "openai",
            "api_key": "NULL",
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
            folder=folder,
            use_vllm=args.vllm,
            vllm_url=args.vllm_url,
            vllm_mode=args.vllm_mode,
            n_iterations=args.iterations,
        )
