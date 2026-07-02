# LLM Opinion Dynamics Simulator (LLM_OD_Llama3.1)

This project simulates opinion dynamics and belief revision within an agent network utilizing Large Language Models (LLMs). The simulator supports both traditional sequential debates (using Autogen) and accelerated parallel batching (using vLLM or Ollama APIs).

---

## Key Features
- **Strict Role Alternation**: Built-in monkeypatch for `pyautogen` and custom async structures to enforce strict `user` / `assistant` alternating roles starting with `user`, preventing `400 BadRequestError` issues on strict LLM servers.
- **vLLM Accelerated Backend**: Speed up simulations up to **100x** by executing all agent debate rounds within an iteration in concurrent batches.
- **Flexible Monitor Modes**: Supports both base `Monitor` rules and neighborhood opinion distribution-aware `MonitorOpinionDistribution` templates.

---

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git checkout vllm
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the LLM Host**:
   - For **Ollama**:
     ```bash
     ollama run google/gemma-3-4b-it
     ```
   - For **vLLM Server**:
     ```bash
     python -m vllm.entrypoints.openai.api_server --model google/gemma-3-4b-it --port 8000
     ```

---

## CLI Usage Reference

Run the simulation from the project root:
```bash
python execution.py <models> <run_n> <theme_name> <exp_name> <n_agents> [<network>] [options]
```

### Positional Arguments
- **`models`**: Comma-separated list of LLM models to use (e.g. `google/gemma-3-4b-it`).
- **`run_n`**: Number of independent stochastic runs of the simulation to perform.
- **`theme_name`**: Filename of the theme JSON file under `themes/` containing the topic statement.
- **`exp_name`**: Experiment name/identifier specifying minority size (e.g., `PAH-min0.1-h0.0`).
- **`n_agents`**: Number of agents to load (e.g. `100`).
- **`network`** *(optional)*: Filename of the graph network edge list CSV. If omitted, a **meanfield** architecture is run.

### Optional Flags
- **`-i`, `--iterations`**: Number of simulation iterations to execute per run. *(Default: `100`)*
- **`--monitor`**: The debate monitor strategy to use. Options: `MonitorOpinionDistribution` or `Monitor`. *(Default: `MonitorOpinionDistribution`)*
- **`--vllm`**: Enables the batched parallel execution engine.
- **`--vllm-url`**: Base API endpoint for the OpenAI-compatible server. *(Default: `http://localhost:8000/v1`)*
- **`--vllm-mode`**: Batching execution mode. Options: `server` (async concurrent requests) or `offline` (runs native Python `vllm` library offline). *(Default: `server`)*

---

## Drop-in Monitor & vLLM Mappings

When the `--vllm` flag is enabled, the CLI automatically maps the requested `--monitor` to its parallel batched equivalent:

| CLI `--monitor` Input | Without `--vllm` (Sequential) | With `--vllm` (Batched Parallel) |
| :--- | :--- | :--- |
| **`MonitorOpinionDistribution`** *(Default)* | `MonitorOpinionDistribution` | `MonitorOpinionDistributionVLLM` |
| **`Monitor`** | `Monitor` | `MonitorVLLM` |

---

## Example Execution Commands

### 1. Traditional Autogen (Sequential) Run
Runs a sequential simulation of 100 agents over 10 iterations using Ollama on port `11434`:
```bash
python execution.py google/gemma-3-4b-it 1 theseus_same.json PAH-min0.1-h0.0 100 PAH-min0.1-h0.0.csv -i 10 --vllm-url http://localhost:11434/v1
```

### 2. Accelerated vLLM (Batched Parallel) Run
Runs a batched parallel simulation of 100 agents over 10 iterations on a vLLM server:
```bash
python execution.py google/gemma-3-4b-it 1 theseus_same.json PAH-min0.1-h0.0 100 PAH-min0.1-h0.0.csv --vllm --vllm-url http://localhost:8000/v1 -i 10
```

### 3. Base Monitor Batched Run
Runs a batched parallel simulation using the base `Monitor` class:
```bash
python execution.py google/gemma-3-4b-it 1 theseus_same.json PAH-min0.1-h0.0 100 PAH-min0.1-h0.0.csv --vllm --monitor Monitor -i 10
```

---

## Detailed Documentation

To view the complete MkDocs project documentation website locally, run:
```bash
pip install mkdocs-material
mkdocs serve
```
Then navigate to `http://127.0.0.1:8000` in your web browser.
