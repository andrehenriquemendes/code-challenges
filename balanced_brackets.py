# https://www.hackerrank.com/challenges/balanced-brackets/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def isBalanced(s):
    stack = []
    
    for c in s:
        if c in ('{', '[', '('):
            stack.append(c)
        else:
            if len(stack) > 0:
                if c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return 'NO'
            else:
                return 'NO'
    
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open('file.txt', 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
