
class Node:
    def __init__(self, value):
        self.data = value
        self.previous = None


def display(fn):
    def operation(*args, **kwargs):
        print(f"Operation={str.upper(fn.__name__)}")
        fn(*args, **kwargs)
        current_node = args[0].top
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.previous
        print("END_OF_STACK\n")
    return operation


class Stack:
    """ Stack using linked list """
    def __init__(self):
        self.top = None

    @display
    def push(self, value):
        new_node = Node(value)

        if self.top is None:
            self.top = new_node
        else:
            new_node.previous = self.top
            self.top = new_node

    @display
    def pop(self):
        if self.top is not None:
            return_value = self.top.data
            self.top = self.top.previous
            return return_value
        else:
            return -1


# Test code to run and see the results
stack = Stack()
stack.pop()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.push(4)
stack.pop()
stack.pop()
stack.pop()
