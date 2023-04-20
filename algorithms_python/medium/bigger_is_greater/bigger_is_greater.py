#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    chars = list(w)

    i = len(chars) - 2
    while i >= 0 and chars[i] >= chars[i + 1]:
        i -= 1

    if i < 0:
        return 'no answer'

    j = len(chars) - 1
    while j > i and chars[j] <= chars[i]:
        j -= 1

    chars[i], chars[j] = chars[j], chars[i]

    chars[i + 1:] = chars[:i:-1]

    return ''.join(chars)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()