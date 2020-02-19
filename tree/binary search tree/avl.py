from .bst import BinarySearchTree
from .bst import TreeNode


class AVLTree(BinarySearchTree):
    def _put(self, key, val, node):
        if key < node.key:
            if node.hasLeftChild():
                self._put(key, val, node.leftChild)
            else:
                node.leftChild = TreeNode(key,val, parent=node)
                self.updateBalanceFactor(node.leftChild)
        else:
            if node.hasRightChild():
                self._put(key, val, node.rightChild)
            else:
                node.rightChild = TreeNode(key, val, parent=node)
                self.updateBalanceFactor(node.rightChild)

    def updateBalanceFactor(self, node):
        if node.balancefactor > 1 or node.balancefactor < -1:
            self.rebalance(node)
            return
        else:
            if node.parent:
                if node.isLeftChild():
                    node.parent.balancefactor += 1
                else:
                    node.parent.balancefactor += 1
                if node.balancefactor !=0:
                    self.rebalance(node.parent)

    def rebalance(self, node):
        if node.balancefactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        else:
            if node.leftChild.balancefactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

    def rotateLeft(self, oldroot):
        newroot = oldroot.rightChild
        oldroot.rightChild = newroot.leftChild
        if newroot.leftChild:
            newroot.leftChild.parent = oldroot
        newroot.parent = oldroot.parent
        if oldroot == self.root:
            self.root = newroot
        else:
            if oldroot.isLeftChild():
                oldroot.parent.leftChild = newroot
            else:
                oldroot.parent.rightChild = newroot
        newroot.leftChild = oldroot
        oldroot.parent = newroot

        oldroot.balancefactor = oldroot.balancefactor + 1 - min(newroot.balancefactor, 0)
        newroot.balancefactor = newroot.balancefactor + 1 + max(oldroot.balancefactor, 0)

    def rotateRight(self, oldroot):
        newroot = oldroot.leftChild
        oldroot.leftChild = newroot.rightChild
        oldroot.leftChild.parent = oldroot
        if oldroot.isRoot():
            self.root = newroot
        else:
            if oldroot.isLeftChild():
                oldroot.parent.leftChild = newroot
            else:
                oldroot.parent.rightChild = newroot
        oldroot.parent = newroot
        newroot.rightChild = oldroot

        oldroot.balancefactor = oldroot.balancefactor + 1 - min(newroot.balancefactor, 0)
        newroot.balancefactor = newroot.balancefactor + 1 + max(oldroot.balancefactor, 0)