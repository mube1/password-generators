# Data-Driven Password Guessing Tools
These are a collection of data driven (based on data) password-guessing tools written in Python. The tools will get smarter as I update them. <br/>
There are a number of datasets out there but here, I used the most common one 'rockyou.txt' which can be downloaded from [here](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

### Use pre-trained
### 2-gram model 
The model is based on bi-gram, collects a sequence of two characters, and calculates probabilities. It has embedded passwords and calculates probabilities 
on the fly as the number of passwords is small relatively.

Run 'python3 password_generator_v1.py m n' ( n passwords of length m  )<br/>

### 4-gram model
This is a better version that is an extention of the first one. It is based on 4-gram. <br/>

-Download a trained 4-gram dic dump (pkl file) [here](https://drive.google.com/file/d/1ZJdEkgRlrGDNgBuU8bMjJsZfS1iFeTKG/view?usp=share_link) <br/>
-pip3 install requirments.txt # (it just contains numpy in case you dont have it)  <br/>
-python3 password_generator_v1.py m n # n amount of passwords with length m  

### Train your own n-gram model <br/>

#### If you want to train your own model, with you  own database:

-train_n_gram.py -o 'output path' -n 'lenght n- gram default is 4' -t 'path to trainset, default is rockyou.txt' <br/>
-It outputs a pkl dump of normalized dict file <br/>
-For inference ngram_inference.py file above<br/>
-To get help, type in python train_n_gram.py -h <br/>
-To run the trained, python3 ngram_inference.py m n m n # n amount of passwords with length m  <br/>
<br/><br/>
### To be posted soon
<br/>
-Training your own dataset for all methods <br/>
-PASSGAN inference based on the [paper](https://arxiv.org/abs/1709.00440)<br/>
-RNN and LSTM-based password guessing for inference <br/>
-GPT-based password guessing for inference <br/>

