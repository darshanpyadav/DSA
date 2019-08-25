class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None

    def insert_start(self, data):
        new_node = Node(data)
        if self.start_node == None:
            self.start_node  = new_node
            return
        else:
            new_node.ref = self.start_node
            self.start_node = new_node
            return

    def insert_end(self, data):
        new_node = Node(data)
        if self.start_node == None:
            self.start_node  = new_node
            return
        else:
            n = self.start_node
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def print_middle_element(self):
        slow = self.start_node
        fast = self.start_node
        while fast is not None and fast.ref is not None:
            fast = fast.ref
            fast = fast.ref
            slow = slow.ref
        print("middle is ", slow.item)

    def delete_element_node(self, data):
        n = self.start_node
        if n.item == data:
            self.start_node = n.ref
            n = None
            return
        while n is not None:
            if n.item == data:
                break
            prev = n
            n = n.ref

        prev.ref = n.ref
        n = None

    def delete_element_pos(self, pos):
        n = self.start_node
        c = 0
        while n is not None:
            c+=1
            print("list at ", c)
            if pos == c:
                break
            prev = n
            n = n.ref
            print("list at ", n.item)
        prev.ref = n.ref
        n = None

    def detect_loop(self, head):
        slow = self.start_node
        fast = self.start_node
        while fast is not None and fast.ref is not None:
            fast=fast.ref
            fast=fast.ref
            slow=slow.ref
            if fast == slow:
                print("True")
                break
            else:
                print("False")

    def print_nth_node(self, n):
        p = self.start_node
        s = self.start_node
        c=0
        while p is not None:
            p = p.ref
            c+=1
        q = c - n
        for i in range(q):
            s = s.ref
        print(s.item)

    def reverse_alt_k_nodes(self, k):
        n = self.start_node


    def delete_last_occ(self, k):
        n = self.start_node
        p = self.start_node
        max =0
        c = 0
        while n is not None:
            if n.item == k:
                print(n.item)
                max = c
            n = n.ref
            c+=1
        print(max)
        LinkedList.delete_element_pos(self,max+1)

    def rotate_list_at_n(self, k):
        curr = self.start_node
        for i in range(k):
            prev = curr
            curr = curr.ref
        while curr.ref is not None:
            curr = curr.ref

        curr.ref = self.start_node
        self.start_node = prev.ref
        prev.ref = None


    def print_list(self):
        n = self.start_node
        c=0
        while n is not None:
            c+=1
            print(n.item,"->")
            n = n.ref

node1 = LinkedList()
node1.insert_start(5)
node1.insert_start(10)
node1.insert_start(15)

node2 = LinkedList()
node2.insert_end(20)
node2.insert_end(30)
node2.insert_end(40)
node2.insert_end(50)
node2.insert_end(60)
node2.insert_end(70)
node2.rotate_list_at_n(3)
node2.print_list()



