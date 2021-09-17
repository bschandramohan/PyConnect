# Linked List Implementation

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class DSList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            # Iterate over list and insert this element at the last
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def print_list(self):
        current_node = self.head
        if current_node is not None:
            print(">> BEGIN")
            while current_node.next is not None:
                print(current_node.data)
                current_node = current_node.next
            print(current_node.data)
            print("<< END\n")
        else:
            print("Empty List")


ds_list = DSList()
ds_list.print_list()
ds_list.insertAtEnd(1)
ds_list.insertAtEnd(2)
ds_list.print_list()
ds_list.insertAtEnd(3)
ds_list.print_list()
