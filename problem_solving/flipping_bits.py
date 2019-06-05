#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the flippingBits function below.
def flippingBits(N):
    N = N & 0xffffffff # 32 bit representation
    x = N ^ 0xffffffff
    return x


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        N = int(input())

        result = flippingBits(N)

        fptr.write(str(result) + '\n')

    fptr.close()
