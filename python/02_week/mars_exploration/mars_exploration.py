#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    message = 'SOS'
    changed_chars = 0

    for i in range(0, len(s)):
        index = i % len(message)
        if s[i] != message[index]:
            changed_chars += 1

    return changed_chars


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
