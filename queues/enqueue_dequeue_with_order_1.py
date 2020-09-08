from linked_lists.append_with_order_1 import LinkedList


class QueueList:
    def __init__(self):
        self.items = LinkedList()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.remove_first_element()

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    q = QueueList()
    q.enqueue("hi")
    print(q)
    q.enqueue("yo")
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)

