# Data driven Password guessing tools
These are a collection of password guessing tools written in python. The tools will get smarter as I update them. <br/>
They are mostly data driven, i.e, they will be based on some data to make the best guess. <br/>
There are a number of datasets out there but here, I used the most common one 'rockyou.txt' which can be downloaded from [here](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

## Use pretrained models
### 2-gram model 
The model is based on bi-gram, collects a sequence of two characters and calculates probabilities.

To run the first file:<br/>
-Download the Rockyou.txt dataset [here](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) <br/>
-Run the command 'python3 password_generator_v1.py m n' ( n passwords of length m  )

### 4-gram model
This is a better version that is an extention of the first one. It is based on 4-gram. <br/>

-Download a trained 4-gram dic dump (pkl file) [here](https://drive.google.com/file/d/1ZJdEkgRlrGDNgBuU8bMjJsZfS1iFeTKG/view?usp=share_link) <br/>
-pip3 install requirments.txt # (it just contains numpy in case you dont have it)  <br/>
-python3 password_generator_v1.py m n # n amount of passwords with length m  

### Train your own n-gram model <br/>

##### If you want to train your own model, with you  own database:

-train_n_gram.py -o 'your path to output the trained dictionary' -n 'lenght n- gram default is 4' -t 'path to trainset, default is rockyou.txt'
-It outputs a pkl file that contains probability values from frequency calculations that can be used for inference ngram_inference.py file above<br/>
-To get help, type in python train_n_gram.py -h

### To be posted soon
<br/><br/>
-Training your own dataset for all methods <br/>
-PASSGAN inference based on the [paper](https://arxiv.org/abs/1709.00440)<br/>
-RNN and LSTM based password guessing for inference <br/>
-GPT based password guessing for inference <br/>

