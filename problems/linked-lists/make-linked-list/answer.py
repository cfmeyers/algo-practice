"""
Make a linked list in Python
See https://realpython.com/linked-lists-python/
"""


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        """
        note: internally convert `data` to a Node
        """
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = node

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def __iter__(self):
        cur_node = self.head
        while cur_node is not None:
            yield cur_node
            cur_node = cur_node.next

    def __repr__(self):
        nodes = [node.item for node in self]
        nodes.append("None")
        return " -> ".join(nodes)


if __name__ == "__main__":
    my_list = LinkedList()
    my_list.add("one")
    my_list.add("two")
    my_list.add("three")
    print(my_list)
    # my_list.reverse()
    # print(my_list)
    # for elem in my_list:
    #     print(elem.item)
