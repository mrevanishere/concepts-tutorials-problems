"""
Try implementing this in C++ also
"""
class Node:
    """
    Node for a Linked List
    """
    next = None
    def __init__(self, data):
        self.data = data

    def push_back(self, data):
        """
        Adds a node to the end of the list
        :param data:
        :return:
        """
        end = Node(data)
        n = self
        while (n.next != None):
            n = n.next
        n.next = end

    def delete_node(self, head, data):
        pass


