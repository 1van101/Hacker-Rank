import math
import os
import random
import re
import sys


def timeConversion(s):
    hours_by_format = {
        'AM': {
            '01': '01',
            '02': '02',
            '03': '03',
            '04': '04',
            '05': '05',
            '06': '06',
            '07': '07',
            '08': '08',
            '09': '09',
            '10': '10',
            '11': '11',
            '12': '00'
        },
        'PM': {
            '01': '13',
            '02': '14',
            '03': '15',
            '04': '16',
            '05': '17',
            '06': '18',
            '07': '19',
            '08': '20',
            '09': '21',
            '10': '22',
            '11': '23',
            '12': '12'
        }
    }

    h, m, s = s.split(':')
    time_format = s[2:]
    seconds = s[:2]

    return f'{hours_by_format[time_format][h]}:{m}:{seconds}'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

