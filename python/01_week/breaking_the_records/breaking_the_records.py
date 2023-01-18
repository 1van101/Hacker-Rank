#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    stats = {'min': {'record': 0, 'count': 0}, 'max': {'record': 0, 'count': 0}}

    for i in range(len(scores)):
        if i == 0:
            stats['min']['record'] = scores[i]
            stats['max']['record'] = scores[i]

        if scores[i] > stats['max']['record']:
            stats['max']['count'] += 1
            stats['max']['record'] = scores[i]

        if scores[i] < stats['min']['record']:
            stats['min']['count'] += 1
            stats['min']['record'] = scores[i]

    return [stats['max']['count'], stats['min']['count']]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
