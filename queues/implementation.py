class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue("hi")
    q.enqueue("yo")
    print(q)
    q.dequeue()
    print(q.size())
    print(q.isEmpty())
    print(q)
