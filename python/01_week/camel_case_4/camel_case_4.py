import sys


def split(word, type):
    res = ''

    if type == 'M':
        word = word[:-2]

    for ch in word:
        if ch.isupper():
            res += ' '
        res += ch

    return res.strip().lower()


def combine(word, type):
    res = ''
    words = word.split()

    if type == 'C':
        return ''.join([word.capitalize() for word in words])

    for i in range(len(words)):
        if i == 0:
            res += words[i]
        else:
            res += words[i].capitalize()

    if type == 'M':
        res += '()'

    return res


# S - split, C - combine
operations = {'S': split, 'C': combine}

# types : M - method, C - class, V - variable


for word in sys.stdin:


    operation, type, word = word.split(';')
    print(operations[operation](word.strip(), type))
