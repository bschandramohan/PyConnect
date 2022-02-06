
class Queue:
    """ Queue using list """
    def __init__(self):
        self.store = []

    def insert(self, data):
        self.store.insert(0, data)

    def remove(self):
        return self.store.pop(-1)

    def print(self):
        print("\nItems in Queue")
        for item in self.store:
            print(item)
        print()


queue = Queue()
queue.insert(10)
queue.insert(20)
queue.insert(30)
queue.print()
print(f"Item removed={queue.remove()}")
print(f"Item removed={queue.remove()}")
queue.print()
