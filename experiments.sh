#/bin/bash

# parameters: model, num_run, theme_name, experiment, number of agents, network

PROMPT_TYPE="theseus_opinion_distr"

# mistral on all minority classes and homophily values (100 agents, 1 iteration)
python execution.py mistral 1 theseus_same.json PAH-min0.5-h0.0 100 PAH-min0.5-h0.0.csv --prompt-type "$PROMPT_TYPE"
echo "PAH-min0.5-h0.0 done" > log.txt
python execution.py mistral 1 theseus_same.json PAH-min0.5-h0.5 100 PAH-min0.5-h0.5.csv --prompt-type "$PROMPT_TYPE"
echo "PAH-min0.5-h0.5 done" > log.txt
python execution.py mistral 1 theseus_same.json PAH-min0.5-h0.25 100 PAH-min0.5-h0.25.csv --prompt-type "$PROMPT_TYPE"
echo "PAH-min0.5-h0.25 done" > log.txt
python execution.py mistral 1 theseus_same.json PAH-min0.5-h0.75 100 PAH-min0.5-h0.75.csv --prompt-type "$PROMPT_TYPE"
echo "PAH-min0.5-h0.5PAH-min0.5-h0.75 done" > log.txt
python execution.py mistral 1 theseus_same.json PAH-min0.5-h1.0 100 PAH-min0.5-h1.0.csv --prompt-type "$PROMPT_TYPE"
echo "PAH-min0.5-h1.0 done" > log.txt

python execution.py mistral 1 theseus_same.json PAH-min0.1-h0.0 100 PAH-min0.1-h0.0.csv --prompt-type "$PROMPT_TYPE"
echo "PAH-min0.1-h0.0 done" > log.txt
python execution.py mistral 1 theseus_same.json PAH-min0.1-h0.5 100 PAH-min0.1-h0.5.csv --prompt-type "$PROMPT_TYPE"
echo "PAH-min0.1-h0.5 done" > log.txt
python execution.py mistral 1 theseus_same.json PAH-min0.1-h0.25 100 PAH-min0.1-h0.25.csv --prompt-type "$PROMPT_TYPE"
echo "PAH-min0.1-h0.25 done" > log.txt
python execution.py mistral 1 theseus_same.json PAH-min0.1-h0.75 100 PAH-min0.1-h0.75.csv --prompt-type "$PROMPT_TYPE"
echo "PAH-min0.1-h0.75 done" > log.txt
python execution.py mistral 1 theseus_same.json PAH-min0.1-h1.0 100 PAH-min0.1-h1.0.csv --prompt-type "$PROMPT_TYPE"
echo "PAH-min0.1-h1.0 done" > log.txt

python execution.py mistral 1 theseus_same.json PAH-min0.3-h0.0 100 PAH-min0.3-h0.0.csv --prompt-type "$PROMPT_TYPE"
echo "PAH-min0.3-h0.0 done" > log.txt
python execution.py mistral 1 theseus_same.json PAH-min0.3-h0.5 100 PAH-min0.3-h0.5.csv --prompt-type "$PROMPT_TYPE"
echo "PAH-min0.3-h0.5 done" > log.txt
python execution.py mistral 1 theseus_same.json PAH-min0.3-h0.25 100 PAH-min0.3-h0.25.csv --prompt-type "$PROMPT_TYPE"
echo "PAH-min0.3-h0.25 done" > log.txt
python execution.py mistral 1 theseus_same.json PAH-min0.3-h0.75 100 PAH-min0.3-h0.75.csv --prompt-type "$PROMPT_TYPE"
echo "PAH-min0.3-h0.75 done" > log.txt
python execution.py mistral 1 theseus_same.json PAH-min0.3-h1.0 100 PAH-min0.3-h1.0.csv --prompt-type "$PROMPT_TYPE"
echo "PAH-min0.3-h1.0 done" > log.txt
