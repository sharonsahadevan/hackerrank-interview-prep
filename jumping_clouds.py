#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    jump = 0
    current = 0
    end = n - 1

    while current < end:
        if ((current + 2) <= end) and (c[current + 2] == 0):
            current += 2
            jump += 1
        elif c[current + 1] == 0:
            current += 1
            jump += 1
    return jump


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
