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
        pass

    def add(self, data):
        """
        note: internally convert `data` to a Node
        """
        pass

    def reverse(self):
        pass

    def __iter__(self):
        pass

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
