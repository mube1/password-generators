import pickle,sys
import numpy as np

with open('normalized_main_stats.pkl', 'rb') as d:
    main_stats = pickle.load(d)

def character_generator(ngrams):
    """ this function takes in a n characters (n-grams) and generates the next char. 
        If the n gram is not in the list, checks a smaller section of it.
    """
    if ngrams in main_stats:
        return np.random.choice(list(main_stats[ngrams].keys()), p=list(main_stats[ngrams].values()) )
    else:
        return character_generator(ngrams[:-1])
        
        
def password(length,gram=4):
    """
    This function takes in a length of the password to be generated, then generates it character by character based on the stats dictionary
    """
    password = '`' * gram
    i=0
    while len(password.replace('`', '')) <length:
        password+=character_generator(password[i:i+gram])
        i+=1
    return password.replace('`', '')


def generate_n(number_of_passwords,length=8):
    passwords=[]
    for i in range(number_of_passwords):
        passwords.append(password(length))
    return passwords

def main():
    length=int(sys.argv[1])
    number_passwords=int(sys.argv[2])
    passwords=generate_n(number_passwords,length)
    print('\n'.join(passwords))
    

if __name__ == "__main__":
    main()