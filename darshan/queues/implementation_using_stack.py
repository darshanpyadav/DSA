from darshan.stacks.implementation import StackList


class QueueUsingStack:
    def __init__(self):
        self.items = StackList()

    def enqueue(self, item):
        self.items.push(item)

    def dequeue(self):
        duplicate_stack = StackList()
        while not self.items.isEmpty():
            duplicate_stack.push(self.items.pop())
        ele = duplicate_stack.pop()
        while not duplicate_stack.isEmpty():
            self.items.push(duplicate_stack.pop())
        return ele

    def size(self):
        return self.items.size()

    def isEmpty(self):
        return self.items.isEmpty()

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    q = QueueUsingStack()
    q.enqueue("1")
    q.enqueue("2")
    q.enqueue("3")
    print(q)
    q.dequeue()
    print(q.size())
    print(q.isEmpty())
    print(q)