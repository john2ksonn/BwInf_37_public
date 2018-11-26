from sys import stdin
from random import randint

#   _____          _     _            
#  |_   ___      _(_)___| |_ ___ _ __ 
#    | | \ \ /\ / | / __| __/ _ | '__|
#    | |  \ V  V /| \__ | ||  __| |   
#    |_|   \_/\_/ |_|___/\__\___|_|   

def start():
    buff = ""
    for line in stdin:
        for ch in line:
            if ch.isalpha():
                buff += ch
            else:
                if len(buff) > 3:
                    print(twist(buff), end="")
                else:
                    print(buff, end="")
                buff = ""
                print(ch, end="")


def twist(arg):
    result, word = cut_char_from_string(arg, 0)
    while len(word) > 1:
        ch, word = cut_char_from_string(word, randint(0, len(word)-2))
        result += ch
    result += word
    return result


def cut_char_from_string(str, idx):
    return str[idx], str[:idx] + str[idx+1:]


if __name__ == "__main__":
    start()

