#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        result = 'Weird'
    elif 2 <= n <= 5:
        result = 'Not Weird'
    elif 6 <= n <= 20:
        result = 'Weird'
    elif n > 20:
        result = 'Not Weird'
    print(result)
