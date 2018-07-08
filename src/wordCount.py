import re

def word_count(str):
    str = str.lower()

    counts = dict()
    #words = str.split()

    rgx = re.compile("([\w][\w']*\w)")
    words = rgx.findall(str)

    #print(words)

    for word in words:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1
    return counts


print(word_count('sachin    asdf sachin asdf neeraj neeraj gupta.\n He is very; famouns for cricket. Cricket is very popular in India'))