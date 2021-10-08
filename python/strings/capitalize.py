#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    outS = list()
    prev_space = False
    for i, c in enumerate(s):
        if i == 0 and c.isalpha():
            outS.append(c.upper())
            continue
        if c == ' ':
            prev_space = True
            outS.append(c)
            continue
        if c.isalpha and prev_space:
            outS.append(c.upper())
            prev_space = False
        else:
            outS.append(c)

    outS = "".join(outS)
    return outS


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    s = '12alan rich'

    result = solve(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
