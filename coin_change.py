#!/usr/bin/python3

import math
import os
import random
import re
import sys

def memoize(f):
    memo = {}
    def helper(*args):
        key = str(args[:2])
        if key not in memo:            
            memo[key] = f(*args)
        return memo[key]
    return helper

@memoize
def calculate_changes(n, m, coins):
    if n == 0: return 1
    elif n < 0 or m < 0: return 0
    else:
        return calculate_changes(n - coins[m], m, coins) + \
        calculate_changes(n, m - 1, coins)

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    coins = list(map(int, input().rstrip().split()))
    print(calculate_changes(n, m - 1, coins))
