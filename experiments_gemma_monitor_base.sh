#!/bin/bash

# parameters: model, num_run, theme_name, experiment, number of agents, network, http

PROMPT_TYPE="theseus"

# gemma3:4b on all minority classes and homophily values (100 agents, 10 iteration)

python execution.py google/gemma-3-4b-it 10 theseus_same.json PAH-min0.1-h0.0 100 PAH-min0.5-h0.0.csv --prompt-type "$PROMPT_TYPE" --monitor Monitor --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h0.0 done" > log_gemma.txt
python execution.py google/gemma-3-4b-it 10 theseus_same.json PAH-min0.1-h0.25 100 PAH-min0.5-h0.25.csv --prompt-type "$PROMPT_TYPE" --monitor Monitor --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h0.25 done" > log_gemma.txt
python execution.py google/gemma-3-4b-it 10 theseus_same.json PAH-min0.1-h0.5 100 PAH-min0.5-h0.5.csv --prompt-type "$PROMPT_TYPE" --monitor Monitor --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h0.5 done" > log_gemma.txt
python execution.py google/gemma-3-4b-it 10 theseus_same.json PAH-min0.1-h0.75 100 PAH-min0.5-h0.75.csv --prompt-type "$PROMPT_TYPE" --monitor Monitor --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h0.75 done" > log_gemma.txt
python execution.py google/gemma-3-4b-it 10 theseus_same.json PAH-min0.1-h1.0 100 PAH-min0.5-h1.0.csv --prompt-type "$PROMPT_TYPE" --monitor Monitor --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h1.0 done" > log_gemma.txt

python execution.py google/gemma-3-4b-it 10 theseus_same.json PAH-min0.1-h0.0 100 PAH-min0.1-h0.0.csv --prompt-type "$PROMPT_TYPE" --monitor Monitor --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h0.0 done" > log_gemma.txt
python execution.py google/gemma-3-4b-it 10 theseus_same.json PAH-min0.1-h0.25 100 PAH-min0.1-h0.25.csv --prompt-type "$PROMPT_TYPE" --monitor Monitor --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h0.25 done" > log_gemma.txt
python execution.py google/gemma-3-4b-it 10 theseus_same.json PAH-min0.1-h0.5 100 PAH-min0.1-h0.5.csv --prompt-type "$PROMPT_TYPE" --monitor Monitor --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h0.5 done" > log_gemma.txt
python execution.py google/gemma-3-4b-it 10 theseus_same.json PAH-min0.1-h0.75 100 PAH-min0.1-h0.75.csv --prompt-type "$PROMPT_TYPE" --monitor Monitor --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h0.75 done" > log_gemma.txt
python execution.py google/gemma-3-4b-it 10 theseus_same.json PAH-min0.1-h1.0 100 PAH-min0.1-h1.0.csv --prompt-type "$PROMPT_TYPE" --monitor Monitor --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.1-h1.0 done" > log_gemma.txt

python execution.py google/gemma-3-4b-it 10 theseus_same.json PAH-min0.3-h0.0 100 PAH-min0.3-h0.0.csv --prompt-type "$PROMPT_TYPE" --monitor Monitor --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.3-h0.0 done" > log_gemma.txt
python execution.py google/gemma-3-4b-it 10 theseus_same.json PAH-min0.3-h0.5 100 PAH-min0.3-h0.5.csv --prompt-type "$PROMPT_TYPE" --monitor Monitor --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.3-h0.5 done" > log_gemma.txt
python execution.py google/gemma-3-4b-it 10 theseus_same.json PAH-min0.3-h0.25 100 PAH-min0.3-h0.25.csv --prompt-type "$PROMPT_TYPE" --monitor Monitor --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.3-h0.25 done" > log_gemma.txt
python execution.py google/gemma-3-4b-it 10 theseus_same.json PAH-min0.3-h0.75 100 PAH-min0.3-h0.75.csv --prompt-type "$PROMPT_TYPE" --monitor Monitor --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.3-h0.75 done" > log_gemma.txt
python execution.py google/gemma-3-4b-it 10 theseus_same.json PAH-min0.3-h1.0 100 PAH-min0.3-h1.0.csv --prompt-type "$PROMPT_TYPE" --monitor Monitor --vllm-mode offline --vllm-url http://127.0.0.1:9996 
echo "PAH-min0.3-h1.0 done" > log_gemma.txt
