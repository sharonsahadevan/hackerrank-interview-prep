#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.


def twoStrings(s1, s2):

    m1 = set(s1)
    m2 = set(s2)

    if set.intersection(m1, m2):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
