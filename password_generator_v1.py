import numpy as np

import re,sys

# sample passwords
text='123456\n12345\n123456789\npassword\niloveyou\nprincess\n1234567\nrockyou\n12345678\nabc123\nnicole\ndaniel\nbabygirl\nmonkey\nlovely\njessica\n654321\nmichael\nashley\nqwerty\n111111\niloveu\n000000\nmichelle\ntigger\nsunshine\nchocolate\npassword1\nsoccer\nanthony\nfriends\nbutterfly\npurple\nangel\njordan\nliverpool\njustin\nloveme\nfuckyou\n123123\nfootball\nsecret\nandrea\ncarlos\njennifer\njoshua\nbubbles\n1234567890\nsuperman\nhannah\namanda\nloveyou\npretty\nbasketball\nandrew\nangels\ntweety\nflower\nplayboy\nhello\nelizabeth\nhottie\ntinkerbell\ncharlie\nsamantha\nbarbie\nchelsea\nlovers\nteamo\njasmine\nbrandon\n666666\nshadow\nmelissa\neminem\nmatthew\nrobert\ndanielle\nforever\nfamily\njonathan\n987654321\ncomputer\nwhatever\ndragon\nvanessa\ncookie\nnaruto\nsummer\nsweety\nspongebob\njoseph\njunior\nsoftball\ntaylor\nyellow\ndaniela\nlauren\nmickey\nprincesa\nalexandra\nalexis\njesus\nestrella\nmiguel\nwilliam\nthomas\nbeautiful\nmylove\nangela\npoohbear\npatrick\niloveme\nsakura\nadrian\nalexander\ndestiny\nchristian\n121212\nsayang\namerica\ndancer\nmonica\nrichard\n112233\nprincess1\n555555\ndi'
data=text.split()

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
    i+=.000001 # to make sure there is not zero sum
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
