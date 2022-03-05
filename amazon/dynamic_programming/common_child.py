# https://www.hackerrank.com/challenges/common-child/problem

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2): # O(2*(n+1)*(m+1)) = O(n*m)
    str_len = len(s1)

    mat = [[0] * (str_len + 1) for _ in range(str_len + 1)] # n+1*m+1
    max_subsequence = 0
    for i in range(1, str_len + 1): # n+1
        for j in range(1, str_len + 1): # m+1
            # print(max_subsequence, end=' ->   ')
            # print(s1[i - 1] + ' == ' + s2[j - 1])
            if s1[i - 1] == s2[j - 1]:
                mat[i][j] = mat[i - 1][j - 1] + 1
            else:
                mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])

    return mat[-1][-1]


if __name__ == '__main__':
    s1 = 'SHINCHAN'
    s2 = 'NOHARAAA'
    print(commonChild(s1, s2))
