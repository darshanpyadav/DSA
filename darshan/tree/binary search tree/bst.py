from pythonds import BinarySearchTree

class TreeNode:
    def __init__(self, key, val, lc=None, rc=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = lc
        self.rightChild = rc
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def isRoot(self):
        return self.parent is None

    def isLeftChild(self):
        return self.parent.leftChild == self

    def isRightChild(self):
        return self.parent.rightChild == self

    def findSuccessor(self):
        if self.hasRightChild():
            succ = self.getMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def getMin(self):
        currentnode = self
        while not currentnode.hasLeftChild():
            currentnode = currentnode.leftChild
        return currentnode

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        else:
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def replaceNodedata(self, key, val, lc, rc, parent):
        self.key = key
        self.payload = val
        self.leftChild = lc
        self.rightChild = rc
        if self.leftChild:
            self.leftChild.parent = self
        if self.rightChild:
            self.rightChild.parent = self


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentnode):
        if key < currentnode.key:
            if currentnode.hasLeftChild():
                self._put(key, val, currentnode.leftChild)
            else:
                currentnode.leftChild = TreeNode(key, val, parent=currentnode)
        else:
            if currentnode.hasRightChild():
                self._put(key, val, currentnode.rightChild)
            else:
                currentnode.rightChild = TreeNode(key, val, parent=currentnode)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentnode):
        if currentnode is None:
            return None
        elif key == currentnode.key:
            return currentnode
        elif key < currentnode.key:
            return self._get(key, currentnode.leftChild)
        else:
            return self._get(key, currentnode.rightChild)

    def __getitem__(self, key):
        res = self.get(key)
        if res:
            return res
        else:
            raise KeyError("No key not in tree")

    def __contains__(self, key):
        res = self.get(key)
        if res:
            return res
        else:
            raise KeyError("No key not in tree")

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def delete(self, key):
        if self.size > 1:
            nodeToDelete = self._get(key, self.root)
            if nodeToDelete:
                self.remove(nodeToDelete)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root == nodeToDelete:
            self.root = None
            self.size = 0
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, currentnode):
        if currentnode.isLeaf():
            if currentnode.isLeftChild():
                currentnode.parent.leftChild = None
            else:
                currentnode.parent.rightChild = None
        elif currentnode.hasBothChildren():
            succ = currentnode.findSuccessor()
            succ.spliceOut()
            currentnode.key = succ.key
            currentnode.payload = succ.payload
        else:
            if currentnode.hasLeftChild():
                if currentnode.isLeftChild():
                    currentnode.parent.leftChild = currentnode.leftChild
                    currentnode.leftChild.parent = currentnode.parent
                elif currentnode.isRightChild():
                    currentnode.parent.rightChild = currentnode.leftChild
                    currentnode.leftChild.parent = currentnode.parent
                else:
                    currentnode.replaceNodedata(currentnode.leftChild.key, currentnode.leftChild.payload, currentnode.leftChild, currentnode.rightChild)
            else:
                if currentnode.isLeftChild():
                    currentnode.parent.leftChild = currentnode.rightChild
                    currentnode.rightChild.parent = currentnode.parent
                elif currentnode.isRightChild():
                    currentnode.parent.rightChild = currentnode.rightChild
                    currentnode.rightChild.parent = currentnode.parent
                else:
                    currentnode.replaceNodedata(currentnode.rightChild.key, currentnode.rightChild.payload, currentnode.leftChild, currentnode.rightChild)