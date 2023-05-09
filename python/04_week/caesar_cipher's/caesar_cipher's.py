#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def add_k(start, end, current, k):
    len_of_alphabet = 26
    ascii_to_add = (current - start + k) % len_of_alphabet + start
    return ascii_to_add

def caesarCipher(s, k):

    s_encrypted = []
    for i in range(len(s)):
        curr_ascii_letter = ord(s[i])


        if curr_ascii_letter in range(65, 91):
            s_encrypted.append(chr(add_k(65, 90, curr_ascii_letter, k)))
        elif curr_ascii_letter in range(97, 123):
            s_encrypted.append(chr(add_k(97, 122, curr_ascii_letter, k)))
        else:
            s_encrypted.append(chr(curr_ascii_letter))
    return ''.join(s_encrypted)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
