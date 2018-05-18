#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import insort

class MedianHeap():
    def __init__(self):
        self.lowers = []
        self.highers = []
        
    def add(self, value):
        if len(self.lowers) == 0 or value < self.lowers[-1]:
            insort(self.lowers, value)
        else:
            insort(self.highers, value)
            
    def rebalance(self):
        if len(self.lowers) > len(self.highers) + 1:
            insort(self.highers, self.lowers.pop())
        elif len(self.highers) > len(self.lowers) + 1:
            insort(self.lowers, self.highers[0])
            del self.highers[0]
    
    def get_median(self):
        if len(self.lowers) > len(self.highers):
            median = float(self.lowers[-1])
        elif len(self.highers) > len(self.lowers):
            median = float(self.highers[0])
        else:
            median = (self.lowers[-1] + self.highers[0]) / 2.0
            
        return median
    
if __name__ == '__main__':
    n = int(input())
    a = MedianHeap()

    for _ in range(n):
        a_item = int(input())
        a.add(a_item)
        a.rebalance()
        print(a.get_median())
            
