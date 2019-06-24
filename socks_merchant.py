#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    socks = collections.Counter(ar)
    pair_count = 0
    for key, value in socks.items():
        if value > 1:
            pair_count += value // 2
    return pair_count


if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
