class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        return

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def add(self, item):
        if not isinstance(item, LinkedNode):
            item = LinkedNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

        return

    def length(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count

    def print(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

        return

    def remove(self, item_id):
        current_id = 1
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_id == item_id:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    return
            previous_node = current_node
            current_node = current_node.next
            current_id += 1

        return

    def unordered_search(self, value):
        current_node = self.head
        node_id = 1
        results = []
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
            current_node = current_node.next

            node_id += 1

        return results

###
# myll = LinkedList()
# myll.add(7)
# myll.add(8)
# myll.add(10)
# myll.add(3)
# myll.add(6)
# myll.remove(2)
# myll.print()
# print(myll.unordered_search(8))
