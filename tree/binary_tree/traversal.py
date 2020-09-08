# *****************************************************************************
# Author            : darshanp (darshanp@juniper.net)
# Date              : 05/10/19
# Last modified by  : darshanp
# Version           : 1.0
# Description       : Let-s-do-it
# *****************************************************************************


def preorder(tree):
    if tree:
        print(tree.get_key())
        preorder(tree.get_left())
        preorder(tree.get_right())


def inorder(tree):
    if tree:
        inorder(tree.get_left())
        print(tree.get_key())
        inorder(tree.get_right())


def postorder(tree):
    if tree:
        postorder(tree.get_left())
        postorder(tree.get_right())
        print(tree.get_key())