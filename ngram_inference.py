import pickle,sys
import numpy as np
import os


def character_generator(ngrams,main_stats):
    """ This function takes in a n characters (n-grams) and generates the next char. 
        If the n gram is not in the list, checks a smaller section of it.
    """
    if ngrams in main_stats:
        return np.random.choice(list(main_stats[ngrams].keys()), p=list(main_stats[ngrams].values()) )
    else:
        return character_generator(ngrams[:-1])

def password(main_stats,length,gram=4):
    """
    This function takes in a length of the password to be generated, then generates it character by character based on the stats dictionary
    """
    password = '`' * gram
    i=0
    while len(password.replace('`', '')) <length:
        password+=character_generator(password[i:i+gram],main_stats)
        i+=1
    return password.replace('`', '')

def generate_n(main_stats,number_of_passwords,length=8):
    passwords=[]
    for i in range(number_of_passwords):
        passwords.append(password(main_stats,length))
    return passwords


def main():
    """ This function parses the command line arguments and calls the generator function """
    length=int(sys.argv[1])
    number_passwords=int(sys.argv[2])
    path=int(sys.argv[3])
    
    assert os.path.exists(path) == True, "File "+path+" doesn't exist"
    
    with open(path, 'rb') as d:
        """ Read trained pkl file of updated dictionaries to calculate probabilites from"""
        main_stats = pickle.load(d)
    passwords=generate_n(main_stats,number_passwords,length)

    print('\n'.join(passwords))
    
if __name__ == "__main__":
    main()