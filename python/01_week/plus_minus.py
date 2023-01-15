import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def print_out(total_count, curr_arr):
    print(f'{len(curr_arr) / total_count:.6f}')


def plusMinus(arr):
    positives = []
    negatives = []
    zeros = []

    for num in arr:
        if num > 0:
            positives.append(num)
        elif num < 0:
            negatives.append(num)
        else:
            zeros.append(num)

    for curr_arr in [positives, negatives, zeros]:
        print_out(len(arr), curr_arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
