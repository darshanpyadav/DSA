from stacks.implementation import Stack


class QueueUsingStack:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.size = 0

    # O(1)
    def enqueue(self, item):
        self.stack1.push(item)
        self.size += 1

    # Amortized O(1) or O(n)
    def dequeue(self):
        if not self.stack2.isEmpty():
            item = self.stack2.pop()
        else:
            for _ in range(self.size):
                self.stack2.push(self.stack1.pop())
            item = self.stack2.pop()
        self.size -= 1
        return item

    def peek(self):
        if not self.stack1.isEmpty():
            return self.stack1.peek()
        elif not self.stack2.isEmpty():
            return self.stack2.peek()
        else:
            return None

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def __str__(self):
        return str(self.stack1) + " " + str(self.stack2)


if __name__ == "__main__":
    q = QueueUsingStack()
    q.enqueue("1")
    print(q.peek())
    q.enqueue("2")
    print(q.peek())
    q.enqueue("3")
    print(q.peek())
    q.enqueue("4")
    print(q.peek())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue("5")
    print(q.peek())
    q.enqueue("6")
    print(q.peek())
    print(q.dequeue())
    print(q.peek())
    print(q.size)
    print(q.isEmpty())
    print(q)
