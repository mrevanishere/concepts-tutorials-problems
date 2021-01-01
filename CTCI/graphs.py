"""
Trees
"""

# Binary Tree
class BTNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        """
        Compare new value with parent node
        :param data:
        :return:
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BTNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BTNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# print node
def visit(node):
    print(node)


# In order traversal Binary Tree
def in_order_traversal(node:BTNode):
    """
    visit left branch, then current node, then right branch
    :param node:
    :return:
    """
    if (node != None):
        in_order_traversal(node.left)
        visit(node)
        in_order_traversal(node.right)


# Pre order BT
def pre_order_traversal(node: BTNode):
    """
    visits current node before child nodes left then right
    :param node:
    :return:
    """
    if (node != None):
        visit(node)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

# Post order BT
def post_order_traversal(node: BTNode):
    """

    :param node:
    :return:
    """
    if(node != None):
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        visit(node)

# define a binary tree
root = BTNode(12)
root.insert(6)
root.insert(14)
root.insert(3)


in_order_traversal(root)
pre_order_traversal(root)
post_order_traversal(root)

"""
Graphs
"""
import queue
class Graph:
    def __init__(self):
        self.nodes = []

class Node:
    def __init__(self, data):
        self.name = data
        self.adj = []

    def __str__(self):
        return str(self.name)


def dfs_reccursive(root: Node):
    """
    root.adj is the adjacency list or matrix  in the graph node class
    :param root:
    :return:
    """
    if (root == None):
        return
    visit(root)
    root.visited = True
    for n in root.adj:
        if (n.visited == False):
            dfs_reccursive(root)

def bfs(root: Node):
    """
    use queue
    :param root:
    :return:
    """
    q = queue.Queue()
    root.visited = True
    q.put(root)
    while not q.empty():
        r = q.get()
        visit(r)
        for n in r.adj:
            n.visited = True
            q.put(n)



