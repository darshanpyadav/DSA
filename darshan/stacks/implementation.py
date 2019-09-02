from pythonds.basic import Stack


class StackList:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    # s = Stack()
    s = StackList()
    s.push(5)
    s.push("hi")
    print(s)
    print(s.peek())
    print(s.size())
    print(s.pop())
    print(s)
    print(s.isEmpty())
