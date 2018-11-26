from sys import stdin
from sys import argv

#   ____       _            _     _            
#  |  _ \  ___| |___      _(_)___| |_ ___ _ __ 
#  | | | |/ _ | __\ \ /\ / | / __| __/ _ | '__|
#  | |_| |  __| |_ \ V  V /| \__ | ||  __| |   
#  |____/ \___|\__| \_/\_/ |_|___/\__\___|_|   


def start():
    buff = ""
    for line in stdin:
        for ch in line:
            if ch.isalpha():
                buff += ch
            else:
                if len(buff) > 3:
                    result = detwist(buff)
                    if 'list' in str(type(result)):
                        if len(result) > 1:
                            print(result,end='')
                        else:
                            if len(result) > 0:
                                print(result[0],end='')
                    else:
                        print(result,end='')
                else:
                    print(buff, end='')
                buff = ""
                print(ch, end='')


def detwist(arg):
    subset = []
    with open(dict_name, 'r', encoding='utf-8') as d:
        # iterate through d
        for word in d:
            # if:
            # * the first letters of the word of d and arg are equal
            # * and their lengths are equal
            # ...
            if word[0].lower() == arg[0].lower() and len(word.strip()) == len(arg):
                # ... check if their last letters are equal ...
                if word[len(word.strip())-1] == arg[len(arg)-1]:
                    # ... calc their checksums ...
                    checksum_word = 0
                    for ch in word.strip().lower():
                        checksum_word += ord(ch)
                    checksum_arg = 0
                    for ch in arg.strip().lower():
                        checksum_arg += ord(ch)
                    # ... and check if the checksums are equal
                    if checksum_word == checksum_arg and not word in subset:
                        # if the checksums are equal append it to the subset
                        subset.append(word)
    # if you are left with only one word, just return it
    if len(subset) == 1:
        return arg[0]+subset[0].strip()[1:]
    # if you are left with more than one word
    # make sure that they have the same letters and the same amount of them
    elif len(subset) > 1:
        subsubset =[]
        for word in subset:
            tmp=True
            for ch in word.strip().lower():
                if not arg.strip().lower().count(ch) == word.strip().lower().count(ch):
                    tmp = False
            # if 'word' has the same letters and amount of them as 'arg'
            # append it to 'subsubset'
            if tmp:
                subsubset.append(arg[0]+word.strip()[1:])
        # finally return subsubset
        return subsubset
    else:
        # if you ended up with no result, just return the twisted word
        return arg.strip()


if __name__ == '__main__':
    dict_name = argv[1]
    start()
