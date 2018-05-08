""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

MIN = 0
MAX = 10**4

def check_subtree(node, minimum, maximum):
    if node is None:
        return True
    elif node.data > minimum and node.data < maximum:
        return check_subtree(node.left, minimum, node.data) and check_subtree(node.right, node.data, maximum)
    return False            

def checkBST(root):
    return check_subtree(root, MIN, MAX)
