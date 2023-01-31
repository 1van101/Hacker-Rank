#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    def factorial(n, num):
        if n == 1:
            return num
        num = num * n

        return factorial(n - 1, num)

    print(factorial(n, 1))


if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
