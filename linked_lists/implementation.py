class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return "value: " + str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, item):
        self.head = Node(item, self.head)

    def append(self, item):
        cur = self.head
        if cur is None:
            self.head = Node(item)
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(item)

    def find(self, item):
        cur = self.head
        while cur is not None and cur.value != item:
            cur = cur.next
        return cur is not None

    def find_element_with_index(self, index):
        cur = self.head
        i = 0
        while cur is not None and i != index:
            cur = cur.next
            i += 1
        return cur

    def remove(self, item):
        prev = None
        cur = self.head
        if cur is None:
            return None
        while cur is not None and cur.value != item:
            prev = cur
            cur = cur.next
        if prev is None:
            self.head = cur.next
        else:
            if cur is not None:
                prev.next = cur.next
        return cur

    # O(n)
    def reverse(self):
        if self.head is None:
            return None

        prev = None
        cur = self.head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    # O(k) -> k = m -n
    def reverse_between_index_m_n(self, m, n):
        m_node = self.find_element_with_index(m)
        n_node = self.find_element_with_index(n - 1)

        n_node_next = n_node.next
        cur = m_node.next
        prev = None

        while cur is not n_node_next:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        a = m_node.next
        a.next = n_node_next
        m_node.next = prev

    def rotate_right_by_k_places(self, k):
        cur = self.head
        l = 0

        while cur.next is not None:
            l += 1
            cur = cur.next
        #  Make it a circular LL
        cur.next = self.head
        cur = cur.next

        for _ in range(l - k):
            cur = cur.next
        self.head = cur.next
        cur.next = None

    def is_empty(self):
        return self.head is None

    def size(self):
        cur = self.head
        length = 0
        while cur is not None:
            cur = cur.next
            length += 1
        return length

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
    l.prepend(1)
    l.append(2)
    l.append(3)
    l.prepend(0)
    l.prepend(-1)
    print(l)
    print(l.find(1))
    print(l.find(4))
    print(l.find_element_with_index(0))
    print("----------------------------")
    l = LinkedList()
    l.prepend(1)
    l.append(2)
    l.append(3)
    l.prepend(0)
    l.prepend(-1)
    l.remove(-1)
    l.remove(3)
    print(l)
    l.append(3)
    l.append(4)
    l.append(5)
    l.append(6)
    l.append(7)
    print(l)
    l.reverse()
    print(l)
    l.rotate_right_by_k_places(3)
    print(l)
    l.reverse_between_index_m_n(1, 6)
    print(l)
