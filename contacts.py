# https://www.hackerrank.com/challenges/contacts/problem
# Trie Data Structure

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#

class Node:

    def __init__(self):
        self.children = {}
        self.end_of_word = False
        self.count = 0


class Trie(object):

    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            child = curr.children.get(c, None)
            if child is None:
                child = Node()
                curr.children[c] = child
            child.count += 1
            curr = child
        curr.end_of_word = True
    

    def _get_count_results(self, term):
        curr = self.root
        for c in term:
            curr = curr.children.get(c)
        return curr.count


    def search(self, term):
        curr = self.root
        for c in term:
            child = curr.children.get(c, None)
            if child is None:
                return 0
            curr = child
        count = self._get_count_results(term)
        return count


def contacts(queries):
    trie = Trie()
    results = []

    for query in queries:
        action = query[0]
        term = query[1]

        if action == 'add':
            trie.insert(term)
        else:
            result = trie.search(term)
            results.append(result)
    
    return results
            


if __name__ == '__main__':
    fptr = open('file.txt', 'w')

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
