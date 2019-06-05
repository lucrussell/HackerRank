#!/bin/python3

import os
import sys


#
# Complete the staircase function below.
#
def staircase(n):
    space_count = n - 1
    spaces = ' ' * space_count
    chars = '#'

    for i in range(0, n):
        line = '{}{}'.format(spaces, chars)
        print(line)
        space_count -= 1
        chars += '#'
        spaces = ' ' * (space_count)


if __name__ == '__main__':
    n = int(input())

    staircase(n)
