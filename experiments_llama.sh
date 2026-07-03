#!/bin/bash

# parameters: model, num_run, theme_name, experiment, number of agents, network, http

PROMPT_TYPE="theseus_opinion_distr"

python execution.py meta-llama/Llama-3.2-3B-Instruct 10 theseus_same.json PAH-min0.1-h0.0 100 PAH-min0.5-h0.0.csv --prompt-type "$PROMPT_TYPE" --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h0.0 done" > log_llama.txt
python execution.py meta-llama/Llama-3.2-3B-Instruct 10 theseus_same.json PAH-min0.1-h0.25 100 PAH-min0.5-h0.25.csv --prompt-type "$PROMPT_TYPE" --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h0.25 done" > log_llama.txt
python execution.py meta-llama/Llama-3.2-3B-Instruct 10 theseus_same.json PAH-min0.1-h0.5 100 PAH-min0.5-h0.5.csv --prompt-type "$PROMPT_TYPE" --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h0.5 done" > log_llama.txt
python execution.py meta-llama/Llama-3.2-3B-Instruct 10 theseus_same.json PAH-min0.1-h0.75 100 PAH-min0.5-h0.75.csv --prompt-type "$PROMPT_TYPE" --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h0.75 done" > log_llama.txt
python execution.py meta-llama/Llama-3.2-3B-Instruct 10 theseus_same.json PAH-min0.1-h1.0 100 PAH-min0.5-h1.0.csv --prompt-type "$PROMPT_TYPE" --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h1.0 done" > log_llama.txt

python execution.py meta-llama/Llama-3.2-3B-Instruct 10 theseus_same.json PAH-min0.1-h0.0 100 PAH-min0.1-h0.0.csv --prompt-type "$PROMPT_TYPE" --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h0.0 done" > log_llama.txt
python execution.py meta-llama/Llama-3.2-3B-Instruct 10 theseus_same.json PAH-min0.1-h0.25 100 PAH-min0.1-h0.25.csv --prompt-type "$PROMPT_TYPE" --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h0.25 done" > log_llama.txt
python execution.py meta-llama/Llama-3.2-3B-Instruct 10 theseus_same.json PAH-min0.1-h0.5 100 PAH-min0.1-h0.5.csv --prompt-type "$PROMPT_TYPE" --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h0.5 done" > log_llama.txt
python execution.py meta-llama/Llama-3.2-3B-Instruct 10 theseus_same.json PAH-min0.1-h0.75 100 PAH-min0.1-h0.75.csv --prompt-type "$PROMPT_TYPE" --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h0.75 done" > log_llama.txt
python execution.py meta-llama/Llama-3.2-3B-Instruct 10 theseus_same.json PAH-min0.1-h1.0 100 PAH-min0.1-h1.0.csv --prompt-type "$PROMPT_TYPE" --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h1.0 done" > log_llama.txt

python execution.py meta-llama/Llama-3.2-3B-Instruct 10 theseus_same.json PAH-min0.3-h0.0 100 PAH-min0.3-h0.0.csv --prompt-type "$PROMPT_TYPE" --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.3-h0.0 done" > log_llama.txt
python execution.py meta-llama/Llama-3.2-3B-Instruct 10 theseus_same.json PAH-min0.3-h0.5 100 PAH-min0.3-h0.5.csv --prompt-type "$PROMPT_TYPE" --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.3-h0.5 done" > log_llama.txt
python execution.py meta-llama/Llama-3.2-3B-Instruct 10 theseus_same.json PAH-min0.3-h0.25 100 PAH-min0.3-h0.25.csv --prompt-type "$PROMPT_TYPE" --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.3-h0.25 done" > log_llama.txt
python execution.py meta-llama/Llama-3.2-3B-Instruct 10 theseus_same.json PAH-min0.3-h0.75 100 PAH-min0.3-h0.75.csv --prompt-type "$PROMPT_TYPE" --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.3-h0.75 done" > log_llama.txt
python execution.py meta-llama/Llama-3.2-3B-Instruct 10 theseus_same.json PAH-min0.3-h1.0 100 PAH-min0.3-h1.0.csv --prompt-type "$PROMPT_TYPE" --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.3-h1.0 done" > log_llama.txt
