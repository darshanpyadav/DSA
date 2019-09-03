class Node:
    def __init__(self, value, data=None):
        self.value = value
        self.next = data


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, item):
        self.head = Node(item, self.head)

    def append(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)

    def find(self, item):
        cur = self.head
        while cur is not None:
            if cur.value == item:
                return cur
            cur = cur.next
        return None

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
        if cur.next is None:
            self.head = None
        while cur is not None and cur.value != item:
            prev = cur
            cur = cur.next
        prev.next = cur.next
        return cur

    # O(n)
    def reverse(self):
        prev = None
        cur = self.head

        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        self.head = cur

    # O(k) -> k = m -n
    def reverse_between_index_m_n(self, m, n):
        m_node = self.find_element_with_index(m-1)
        n_node = self.find_element_with_index(n-1)

        cur = m_node.next
        prev = None

        while cur is not n_node.next:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        cur.next = m_node
        m_node.next.next = n_node

    def rotate_list_by_k_places(self, k):
        cur = self.head
        for i in range(1, self.size() + 1):
            if i == (self.size() - k):
                next = cur.next
                cur.next = None
                cur = next
                continue
            cur = cur.next
        cur.next = self.head

    def is_empty(self):
        return self.head == None

    def size(self):
        temp = self.head
        length = 0
        while temp.next is not None:
            temp = temp.next
            length += 1
        return length
