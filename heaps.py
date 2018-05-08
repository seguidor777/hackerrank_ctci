import sys

class Heap:
    def __init__(self, items):
        self.items = items
        
    def parent(self, index):
        self.items[index - 1 / 2]
        
    def left_child(self, index):
      self.items[index * 2 + 1]
    
    def right_child(self, index):
      self.items[index * 2 + 2]
    
    def poll(self):
        heapify_down()
    
    def append(self, value):
        heapify_up()
    
    def heapify_down(self):
        pass
    
    def heapify_up(self):
        pass
    
    def median(self):
        pass
    
n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
   a_t = int(input().strip())
   a.append(a_t)
heap = Heap(a)
print(heap.median())
