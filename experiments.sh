#/bin/bash

#### Theseus reverse
#python execution.py llama3,mistral 1 theseus_same.json peel-A 40 peel-A.csv
#echo "peel-A done" > log.txt
#python execution.py llama3,mistral 1 theseus_same.json peel-B 40 peel-B.csv
#echo "peel-B done" > log.txt
#python execution.py llama3,mistral 1 theseus_same.json peel-C 40 peel-C.csv
#echo "peel-C done" > log.txt
#python execution.py llama3,mistral 1 theseus_same.json peel-D 40 peel-D.csv
#echo "peel-D done" > log.txt
#python execution.py llama3,mistral 1 theseus_same.json peel-E 40 peel-E.csv
#echo "peel-E done" > log.txt

#### Theseus
#python execution.py mistral,llama3 1 theseus_same.json peel-A 40 peel-A.csv
#echo "peel-A done" > log.txt
#python execution.py mistral,llama3 1 theseus_same.json peel-B 40 peel-B.csv
#echo "peel-B done" > log.txt
#python execution.py mistral,llama3 1 theseus_same.json peel-C 40 peel-C.csv
#echo "peel-C done" > log.txt
#python execution.py mistral,llama3 1 theseus_same.json peel-D 40 peel-D.csv
#echo "peel-D done" > log.txt
#python execution.py mistral,llama3 1 theseus_same.json peel-E 40 peel-E.csv
#echo "peel-E done" > log.txt

#### RED
# python execution.py mistral,llama3 1 red.json peel-A 40 peel-A.csv
# echo "red peel-A done" > log.txt
# python execution.py mistral,llama3 1 red.json peel-B 40 peel-B.csv
# echo "red peel-B done" > log.txt
# python execution.py mistral,llama3 1 red.json peel-C 40 peel-C.csv
# echo "red peel-C done" > log.txt
# python execution.py mistral,llama3 1 red.json peel-D 40 peel-D.csv
# echo "red peel-D done" > log.txt
# python execution.py mistral,llama3 1 red.json peel-E 40 peel-E.csv
# echo "red peel-E done" > log.txt

#### RED reverse
python execution.py llama3.1 1 theseus_same.json PAH-min0.3-h0.0 100 PAH-min0.3-h0.0.csv
echo "PAH-min0.5-h0.0 done" > log.txt
python execution.py llama3.1 1 theseus_same.json PAH-min0.3-h0.5 100 PAH-min0.3-h0.5.csv
echo "PAH-min0.5-h0.5 done" > log.txt
python execution.py llama3.1 1 theseus_same.json PAH-min0.3-h0.25 100 PAH-min0.3-h0.25.csv
echo "PAH-min0.5-h0.25 done" > log.txt
python execution.py llama3.1 1 theseus_same.json PAH-min0.3-h0.75 100 PAH-min0.3-h0.75.csv
echo "PAH-min0.5-h0.5PAH-min0.5-h0.75 done" > log.txt
python execution.py llama3.1 1 theseus_same.json PAH-min0.3-h1.0 100 PAH-min0.3-h1.0.csv
echo "PAH-min0.5-h1.0 done" > log.txt
