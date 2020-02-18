# *****************************************************************************
# Author            : darshanp (darshanp@juniper.net)
# Date              : 05/10/19
# Last modified by  : darshanp
# Version           : 1.0
# Description       : Let-s-do-it
# *****************************************************************************

COUNT = 10


class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.key = data

    def insert_left(self, data):
        if self.left is None:
            self.left = BinaryTree(data)
        else:
            l = BinaryTree(data)
            l.left = self.left
            self.left = l

    def insert_right(self, data):
        if self.right is None:
            self.right = BinaryTree(data)
        else:
            r = BinaryTree(data)
            r.right = self.right
            self.right = r

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_key(self):
        return self.key

    def preorder(self):
        print(self.get_key())
        if self.get_left():
            self.get_left().preorder()
        if self.get_right():
            self.get_right().preorder()

    def inorder(self):
        if self.get_left():
            self.get_left().inorder()
        print(self.get_key())
        if self.get_right():
            self.get_right().inorder()

    def postorder(self):
        if self.get_left():
            self.get_left().postorder()
        if self.get_right():
            self.get_right().postorder()
        print(self.get_key())

    def __str__(self, level=0):
        ret = "\n\t" + self.key
        l = self.get_left().__str__()
        r = self.get_right().__str__()
        return ret + l + r


def print_tree(root, space=0):
    # Base case
    if root is None:
        return

    # Increase distance between levels
    space += COUNT

    # Process right child first
    print_tree(root.get_right(), space)

    # Print current node after space count
    for i in range(COUNT, space):
        print(end=" ")
    print(root.key, end="\n")

    # Process left child
    print_tree(root.get_left(), space)


tree = BinaryTree('r')
tree.insert_left('b')
tree.insert_right('c')
tree.get_left().insert_right('d')
tree.get_right().insert_left('e')
tree.get_right().insert_right('f')
print_tree(tree)
