"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    if head is None: return False
    visited_nodes = []
    current = head
    
    while current is not None:
        if current in visited_nodes:
            return True
        else:
            visited_nodes.append(current)
        current = current.next
        
    return False
