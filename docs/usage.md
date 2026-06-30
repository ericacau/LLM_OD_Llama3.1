# Usage Guide

This page details how to configure and execute opinion dynamics simulations using the CLI interface.

---

## Command Syntax

The simulation is started using the `execution.py` script:

```bash
python execution.py <models> <run_n> <theme_name> <exp_name> <n_agents> [<network>] [options]
```

### Positional Arguments

| Argument | Type | Description |
| :--- | :--- | :--- |
| `models` | `string` | Comma-separated list of LLM models to use (e.g. `llama3.1:latest` or `mistral`). The model name must match the `llm_name` parameter defined in the agent profile files. |
| `run_n` | `int` | The number of independent simulation runs to perform (creates files with suffix `_0`, `_1` ... `_N`). |
| `theme_name` | `string` | File name of the theme JSON file stored in `themes/` (e.g., `theseus_same.json`). |
| `exp_name` | `string` | Experiment code specifying the configuration format. Must contain the minority fraction (e.g., `PAH-min0.5-h0.0`). |
| `n_agents` | `int` | Number of agents to load (e.g., `100`). The script loads agent profiles from `sample_data/agents_<exp_name>_<n_agents>_<models>.json`. |
| `network` | `string` *(optional)* | Filename of the graph network edge list located in `data/min<minority_size>/` (e.g., `PAH-min0.5-h0.0.csv`). If omitted, the simulation defaults to a **meanfield** model where agents interact with random participants instead of network neighbors. |

---

## Optional Arguments

| Flag | Value Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `-h`, `--help` | N/A | N/A | Show help message and exit. |
| `--vllm` | N/A | Disabled | Toggle the batched parallel execution mode. |
| `--vllm-url` | `string` | `http://localhost:8000/v1` | Base API endpoint for the OpenAI-compatible vLLM/Ollama server. |
| `--vllm-mode` | `string` | `server` | Batching execution mode. Options: `server` (async concurrent requests) or `offline` (runs native `vllm` package offline). |
| `-i`, `--iterations` | `int` | `100` | Number of simulation iterations to run. |

---

## Example Executions

### Running a Default (Sequential Autogen) Simulation
To run a single run of the default sequential simulation with 100 agents, 100 iterations, using Ollama on port `11434`:

```bash
python execution.py mistral 1 theseus_same.json PAH-min0.5-h0.0 100 PAH-min0.5-h0.0.csv -i 100
```

### Running with vLLM (Batched Server Mode)
To accelerate the same run using the parallel vLLM backend pointing to local Ollama (highly concurrent) or a running vLLM server:

```bash
python execution.py llama3.1:latest 1 theseus_same.json PAH-min0.5-h0.0 100 PAH-min0.5-h0.0.csv --vllm --vllm-url http://localhost:11434/v1 -i 100
```
*(Here, we use the `llama3.1:latest` model on local Ollama, running all agent interactions concurrently).*
