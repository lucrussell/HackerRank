#!/bin/python3

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    pos = []
    neg = []
    zeros = []
    for i in arr:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
        else:
            zeros.append(i)
    print('{0:.6f}'.format(len(pos)/len(arr)))
    print('{0:.6f}'.format(len(neg)/len(arr)))
    print('{0:.6f}'.format(len(zeros)/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
