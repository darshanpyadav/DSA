# *****************************************************************************
# Author            : darshanp (darshanp@juniper.net)
# Date              : 15/10/19
# Last modified by  : darshanp
# Version           : 1.0
# Description       : Let-s-do-it
# *****************************************************************************


class MaxBinaryHeap:
    def __init__(self):
        self.list = [0]
        self.size = 0

    def insert(self, data):
        self.list.append(data)
        self.size += 1
        self.move_up(self.size)

    def move_up(self, size):
        # moving up, parents are found at n//2
        while size // 2 > 0:
            if self.list[size // 2] < self.list[size]:
                self.list[size // 2], self.list[size] = self.list[size], self.list[size // 2]
            size //= 2

    def get_max(self):
        return self.list[1]

    def delete_max(self):
        ele = self.list[1]
        self.list[1] = self.list[self.size]
        self.size -= 1
        self.move_down(1)
        return ele

    def move_down(self, i):
        # moving down, children are found at 2*i
        while 2 * i <= self.size:
            max_index = self.get_max_index(i)
            if self.list[i] < self.list[max_index]:
                self.list[i], self.list[max_index] = self.list[max_index], self.list[i]
            i = max_index

    def get_max_index(self, i):
        if 2 * i + 1 > self.size:
            return self.list[2 * i]
        return 2 * i if self.list[2 * i] >= self.list[2 * i + 1] else 2 * i + 1

    def build_from_list(self, l):
        self.list = [0] + l[:]
        self.size = len(l)
        i = len(l) // 2  # sort each levels from bottom up
        while i > 0:
            self.move_down(i)
            i -= 1


b = MaxBinaryHeap()
b.build_from_list([9, 5, 6, 2, 3])
b.insert(8)
b.insert(7)

print(b.delete_max())
print(b.delete_max())
print(b.delete_max())
print(b.delete_max())
print(b.delete_max())
print(b.delete_max())
print(b.delete_max())
