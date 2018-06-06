import queue
from collections import defaultdict

class Graph:        
    def __init__(self, n):
        self.n = n
        self.adjacents = defaultdict(list)
    
    def connect(self, x, y):
        self.adjacents[x].append(y)
        self.adjacents[y].append(x)
    
    def find_all_distances(self, s):
        distances = [-1 for i in range(self.n)]
        distances[s] = 0
        visited = {s}
        next_to_visit = queue.Queue()
        next_to_visit.put(s)

        while not next_to_visit.empty():
            node = next_to_visit.get()
            distance = distances[node]
            
            for adjacent in self.adjacents[node]:
                if adjacent not in visited:
                    distances[adjacent] = distance + 6
                    visited.add(adjacent)
                    next_to_visit.put(adjacent)
                    
        distances.pop(s)
        print(" ".join(map(str, distances)))

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1) 
    s = int(input())
    graph.find_all_distances(s - 1)
