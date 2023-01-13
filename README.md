# password-generators
This is a simple password generator project.
Assumes there is 'rockyou.txt' file in the same path as the file. The file can be found online or .

# Use pretrained models
## 2-gram model 
The model is based on bi-gram, collects a sequence of two characters and calculates probabilities.

To run the first file:
-Download the Rockyou.txt dataset[here](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) 
-Run the command 'python3 password_generator_v1.py m n' ( n passwords of length m  )

## 4-gram model
This is a better version that is an extention of the first one. It is based on 4-gram. Some codes are adapted from ...  

### To train from scratch
-Download the Rockyou.txt dataset[here](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)   
-Adjust the path of Rockyou.txt file in the train file Train_n_gram_password.ipynb

### To run already trained
-Download [this](https://drive.google.com/file/d/1ZJdEkgRlrGDNgBuU8bMjJsZfS1iFeTKG/view?usp=share_link) file in the same folder as  password_generator_v2.py file
-Run pip3 install requirments.txt (it just contains numpy in case you dont have it)  
-Run the command 'python3 password_generator_v1.py m n' ( n passwords of length m  )  

# Train new models

