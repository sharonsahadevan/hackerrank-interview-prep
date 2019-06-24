#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.


def checkMagazine(magazine, note):
    magazine_dict = dict()

    for word in magazine:
        if magazine_dict.get(word) != None:
            if magazine_dict[word] > 0:
                magazine_dict[word] += 1
        else:
            magazine_dict[word] = 1

    for k in note:
        if magazine_dict.get(k) is None or magazine_dict[k] == 0:
            return False
        else:
            magazine_dict[k] -= 1
    return True


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    answer = checkMagazine(magazine, note)
    if answer:
        print("Yes")
    else:
        print("No")
