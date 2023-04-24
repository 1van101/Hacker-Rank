#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def is_non_degenerate(a, b, c):
    if all([a + b > c, a + c > b, b + c > a]):
        return True
    return False


def maximumPerimeterTriangle(sticks):
    sticks.sort(reverse=True)
    for i in range(len(sticks) - 2):
        a, b, c = [sticks[i], sticks[i + 1], sticks[i + 2]]
        if is_non_degenerate(a, b, c):
            return (c, b, a)
    return [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
