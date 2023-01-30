#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    all_nums = {}

    for num in a:
        try:
            all_nums[num] += 1
        except KeyError:
            all_nums[num] = 1

    return ''.join(list(str(n) for n in all_nums if all_nums[n] == 1))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
