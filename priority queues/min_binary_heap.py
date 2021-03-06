# *****************************************************************************
# Author            : darshanp (darshanp@juniper.net)
# Date              : 09/10/19
# Last modified by  : darshanp
# Version           : 1.0
# Description       : Let-s-do-it
# *****************************************************************************
from pythonds import BinHeap


class MinBinaryHeap:
    def __init__(self):
        self.list = [0]
        self.size = 0

    def insert(self, ele):
        # O(logN)
        self.list.append(ele)
        self.size += 1
        self.move_up(self.size)

    def move_up(self, size):
        while size // 2 > 0:
            if self.list[size] < self.list[size // 2]:
                self.list[size], self.list[size // 2] = self.list[size // 2], self.list[size]
            size //= 2

    def get_min(self):
        return self.list[1]

    def delete_min(self):
        # O(logN)
        # No of nodes in a complete binary tree 2^l-1 (n is levels).
        # No of levels = log(nodes + 1) base2
        del_item = self.list[1]
        self.list[1] = self.list[self.size]
        self.size -= 1
        self.move_down(1)
        return del_item

    def move_down(self, i):
        while 2 * i <= self.size:
            min_index = self.get_min_index(i)
            if self.list[i] > self.list[min_index]:
                self.list[i], self.list[min_index] = self.list[min_index], self.list[i]
            i = min_index

    def get_min_index(self, i):
        if 2 * i + 1 > self.size:
            return 2 * i
        return 2 * i if self.list[2 * i] <= self.list[2 * i + 1] else 2 * i + 1

    def build_from_list(self, l):
        # O(N/2*logN/2)
        if len(self.list) == 1:
            self.list = [0] + l[:]
            self.size = len(l)
        else:
            self.list = self.list + l[:]
            self.size += len(l)
        i = self.size // 2  # parents will be at l//2. Start from i till 0
        while i > 0:
            self.move_down(i)
            i -= 1

    def __str__(self):
        return str(self.list)


b = MinBinaryHeap()
# b.build_from_list([9, 5, 6, 2, 3])
# b.insert(8)
# b.insert(7)
# print(b.delete_min())
# print(b.delete_min())
# print(b.delete_min())
# print(b.delete_min())
# print(b.delete_min())
# print(b.delete_min())
# print(b.delete_min())

b.build_from_list([[1, 10, 20], [4, 11, 13], [3, 8, 9]])
# b.build_from_list([4, 11, 13])
# b.build_from_list([3, 8, 9])

for i in range(9):
    print(b.delete_min())