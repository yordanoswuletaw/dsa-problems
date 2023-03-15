#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    
    cSum = str(sum(map(int, n)))
    if len(cSum) > 1:
        return superDigit(cSum, k)
    else:
        cSum = str(k * int(cSum))
        # to not multiplay the comulative sum with k again
        k = 1
        if len(cSum) > 1:
            return superDigit(cSum, k)
        else:
            return cSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
