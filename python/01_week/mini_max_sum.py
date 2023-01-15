#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    values = []
    for num in range(len(arr)):
        curr_value = []

        while len(curr_value) != 4:
            curr_value.append(arr[num % len(arr)])
            num += 1
        values.append(sum(curr_value))

    print(min(values), max(values))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
