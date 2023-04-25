#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort()

    nums_reps = {x: a.count(x) for x in a}
    keys = list(nums_reps.keys())
    max_diff = nums_reps[keys[0]]

    for i in range(len(nums_reps) - 1):
        if nums_reps[keys[i]] > max_diff:
            max_diff = nums_reps[keys[i]]

        abs_diff = abs(keys[i] - keys[i + 1])
        result = nums_reps[keys[i]] + nums_reps[keys[i + 1]]

        if abs_diff <= 1 and result > max_diff:
            max_diff = nums_reps[keys[i]] + nums_reps[keys[i + 1]]

    return max_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
