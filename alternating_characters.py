#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    count_adj = 0
    i = 0
    while i < len(s): 
        curr_char = s[i] 
        j = i + 1
        while j < len(s) and s[j] == curr_char:
            count_adj += 1
            j += 1
        i = j
    
    return count_adj

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
