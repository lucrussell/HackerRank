#!/bin/python3

import os
import sys

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    primary = 0
    secondary = 0
    for row_idx, row in enumerate(a):
        print('{} {}'.format(row_idx, row))
        primary += row[row_idx]
        secondary += row[len(a)-1 - row_idx]
    print(primary)
    print(secondary)
    return abs(primary - secondary)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()
