
import re, pickle,argparse,os
from operator import concat
from tqdm import tqdm

parser = argparse.ArgumentParser(
    prog =__file__,
    description = 'This piece of code trains an N-gram password guessing model'
    )
parser.add_argument(
    '-n', 
    '--ngram',
    type=int,
    help='An integer for the N-gram calculator',
    default =4
    )  

parser.add_argument("-o", "--output", 
            default='normalized_main_stats.pkl',
            type=str,
            help='Path to the dict to be saved after training'
            )

parser.add_argument("trainset", 
            type=str,
            help='The path to the train set',
            default='https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt',
            )

args = parser.parse_args()
assert args.output[-3:]=='pkl', 'The output has to be in pickle format .pkl'
assert args.ngram<=1, 'Too small N value for n gram'
assert os.path.exists(args.trainset) == True, "File "+args.trainset+" doesn't exist"

n=args.ngram



# READ THE FILE
file=open(args.trainset,  encoding='latin-1')

with open(args.trainset,  encoding='latin-1') as f:
    text = f.read()

all_passwords=text.split()


#given a string and a length, return ngrams, substrings of length n
ngrammar =lambda word,n:re.findall("(?=("+n*'.' + "))", word)

def word_processor(word,n):
    """
    GIVEN A WORD (A SINGLE PASSWORD) AND RETURNS THEIR GRAMS WITH THEIR LABELS
    """
    init_grams=[('`'*(n-i)+word[0:i],word[i]) for i in range(n)]
    #These are intitial grams with '`'
    
    ngrams=list(map(lambda l:(l[:-1],l[-1]),list(map(concat, ngrammar(word,n),\
                                          list(map(lambda n:n[-1],ngrammar(word,n+1)))))))
    
    return init_grams + ngrams

# KEEP THE SEGMENTS IN A DICTIONARY
main_statstics={}
main_statstics


# GIVEN DATA POINTS OF A SINGLE PASSWORD, THIS WILL UPDATE THE MAIN DICTIONARY CREATED
def update_stats(list_of_points):
    for i in list_of_points:
        if i[0] not in main_statstics:
            main_statstics[i[0]] = {}
            main_statstics[i[0]][i[1]]=0
        else:
            if i[1] not in main_statstics[i[0]]:                
                main_statstics[i[0]][i[1]]=0
                    
        main_statstics[i[0]][i[1]]+=1            


# THE WHOLE CHARSET, 
char_space=set('a')

# THE MAIN LOOP THAT DOES EVERYTHING
for a_password in tqdm(all):
    # update char_space
    char_space=char_space | set(a_password)

    # for a single password, this gets labeled n-grams as a list of tuples[(ngra,label)]
    all_n_grams=[word_processor(a_password,min(len(a_password),i)) for i in (1,n+1)]

    # UPDATES FREUNCIES
    update_stats(all_n_grams)

def convert_stats_to_probabilities(stats):
# convert frequency counts to probabilities
    for ngram in stats:

        chars = []
        occur = []
        probs = []

        for key, value in stats[ngram].items():
            chars.append(key)
            occur.append(value)

        total = sum(occur)
        probs = [float(x) / float(total) for x in occur]

        for key, value in stats[ngram].items():
            stats[ngram][key] = float(value) / float(total)

# SAVE BOTH DICTIONARIES ( COUNTED AND NORMALIZED INTO PROBABILITES)


#Update statstics
convert_stats_to_probabilities(main_statstics)

with open(args.output, 'wb') as s:
    pickle.dump(main_statstics, s)