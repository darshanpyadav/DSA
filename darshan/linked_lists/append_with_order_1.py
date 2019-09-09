class Node:
    def __init__(self, value, data=None):
        self.value = value
        self.next = data

    def __str__(self):
        return "value: " + str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, item):
        cur = self.head
        if cur is None:
            self.head = self.last = Node(item)
        else:
            self.last.next = Node(item)
            self.last = self.last.next

    def remove_first_element(self):
        cur = self.head
        if cur is None:
            return None
        if cur == self.last:
            self.head = self.last = None
        else:
            self.head = cur.next

    def __str__(self):
        cur = self.head
        res = ""
        if cur is None:
            res = "[]"
        else:
            res = "[ "
            while cur.next is not None:
                res += str(cur.value) + " -> "
                cur = cur.next
            res += str(cur.value) + " ]"
        return res


if __name__ == "__main__":
    l = LinkedList()
    l.append(1)
    print(l)
    l.append(2)
    print(l)
    l.append(3)
    print(l)
    l.remove_first_element()
    print(l)
    l.remove_first_element()
    print(l)
    l.remove_first_element()
    print(l)
    print("----------------------------")
