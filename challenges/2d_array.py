#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    hg_sums = []
    for x in range(1, 5):
        hg = 0
        for y in range(1, 5):
            hg = arr[x][y]
            hg += arr[x - 1][y]
            hg += arr[x - 1][y - 1]
            hg += arr[x - 1][y + 1]
            hg += arr[x + 1][y]
            hg += arr[x + 1][y - 1]
            hg += arr[x + 1][y + 1]
            hg_sums.append(hg)
    return max(hg_sums)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
