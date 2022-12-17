import numpy as np
# import random as rm
import re,sys

data=[]
path='rockyou.txt'
data_size=10000
with open(path) as fin:
    fin.seek(0)
    l=0
    while fin:    
        temp= fin.readline()
        data.append(temp)
        l+=len(data[-1])
        fin.seek(l)
        if len(data)>=data_size:
            break


bigrammer = lambda word: re.findall("(?=(..))", word) 

all_chars=set(data[0])
for i in data:
    all_chars=all_chars | set(i)
    
all_bigrams={}
for i in data:
    temp=bigrammer(i)
    for j in temp:
        try:
            all_bigrams[j]+=1
        except:
            all_bigrams[j]=1     

Chars=list(all_chars)

main_matrix=np.zeros((len(all_chars),len(all_chars)))

for i in range(len(all_chars)):
    for j in range(len(all_chars)):
        try:
            idx=Chars[i]+Chars[j]

            main_matrix[i][j]=all_bigrams[idx]
        except:
            main_matrix[i][j]=0

for i in main_matrix:
    i+=.000001 # to make sure there is not zer sum
    i/=i.sum()

def generator(ch):
    state_idx=Chars.index(ch)
    try:
        change=np.random.choice(Chars,replace=True,p=main_matrix[state_idx])    
    except:
        state_idx=Chars.index('e')
        change=np.random.choice(Chars,replace=True,p=main_matrix[state_idx])
    v=Chars.index(change)
    return main_matrix[state_idx][v],Chars[v]

def password(first='p',length=8):
    prob = 1
    i=0
    pwd=first
    while i<length:
        p,first=generator(first)
        prob*=p
        pwd+=first
        i+=1
    return pwd
def generate_n(number_of_passwords,length=8):
    return [password(Chars[np.random.randint(len(Chars))],length) for i in range(number_of_passwords)]

def main():
    length=int(sys.argv[1])
    number_passwords=int(sys.argv[2])

    passwords=generate_n(number_passwords,length)

    print('\n'.join(passwords))

if __name__ == "__main__":
    main()