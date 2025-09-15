# LLM_OD_Llama3.1

## Updates
- Old run of the experiments are in /results/OLD
- Monitor type is now set to the new "theseus_opinion_distr"
- execution.py has been modified to avoid the presence of \r with agent IDs
- 


## Additional stuff:
- The code automatically runs "reverse" simulations, to run the "normal version" remove "reverse_" from
  agent_file = f"sample_data/reverse_agents_{experiment}_{n_agents}_llama3.json"
- Results are stored into "results/minority_class/". This path contains both reverse and "base" experiments

Experiments 
Base: 
 - Blue: minority class
 - Red: majority class

Reverse:
 - Blue: majority class
 - Red: minority class
