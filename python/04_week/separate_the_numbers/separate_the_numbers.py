#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    if s[0] == '0' or len(s) == 1:
        print('NO')
        return


    for i in range(1, len(s) + 1):
        first_num = s[:i]
        curr_num = s[:i]
        temporary = curr_num
        while len(temporary) < len(s):
            curr_num = str(int(curr_num) + 1)
            temporary += curr_num

        if temporary == s and len(first_num) != len(s):
            print('YES', first_num)
            return

    print('NO')

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
