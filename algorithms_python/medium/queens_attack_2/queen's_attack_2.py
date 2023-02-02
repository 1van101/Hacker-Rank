#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def is_valid_index(r, c, n):
    return all([r in range(1, n + 1), c in range(1, n + 1)])


def queensAttack(n, k, r_q, c_q, obstacles):
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    moves = 0
    r = r_q
    c = c_q
    obstacles = set(tuple(x) for x in obstacles)

    for dir in directions:
        r += dir[0]
        c += dir[1]
        while is_valid_index(r, c, n):
            if (r, c) in obstacles:
                break

            moves += 1
            r += dir[0]
            c += dir[1]
        r = r_q
        c = c_q



    return moves

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
