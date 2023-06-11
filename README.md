# Semantle Solver

Open semantle.com and a terminal (after copying the repo).
First, run `pip3 install -r requirements.txt`. Then, run `python3 solver.py`. The first time you run the program it will need to download a 3.6GB dataset (make sure you have space otherwise you'll receive an OSError). After the first download it won't need to download again and will run much faster. Follow the command line prompts by entering in the word you need to guess into semantle.com. The answer should be found within 3 guesses (1 or 2 if you're really lucky). On the off chance it takes 4 guesses or there is an error, raise an issue!

The `simulator.py` is a program to simulate the semantle.com game for testing. Run `python3 simulator.py manual` if you want to enter your own word or `python3 simulator.py automatic` if you want to use a random word.

`wordsearch.py` is a program that finds the best starting word. It takes 91 hours to run on an M1 and I'm too lazy but if you have a better computer or a cluster feel free to run it and tell me what the theoretical best starting word is. Doesn't matter in practice but might matter if playing a version of semantle without filtering words...and I can't imagine why someone would do that since a surprising proportion of the dataset is random names and obscure phrases.
