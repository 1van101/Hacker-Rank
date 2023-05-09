#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    arr.sort()
    pairs = {(arr[i], arr[i + 1]): abs(arr[i] - arr[i + 1])  for i in range(0, len(arr) - 1)}

    min_sum = min(pairs.values())

    pairs_filtered = [x for y in pairs.keys() for x in y if pairs[y] == min_sum]

    return pairs_filtered

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
