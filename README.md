# password-generators
This is a simple password generator project.
Assumes there is 'rockyou.txt' file in the same path as the file. The file can be found online or [here](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt).


It generates n passwords of length m where n and m are to be given as arguments. The model is based on bi-gram, collects a sequence of two characters and calculates probabilities.


To try it, run python3 password_generator_v1.py m n.
