# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def compareLeafTraversal(tree1, tree2):
    treeOneLeaves = []
    treeTwoLeaves = []
    getLeafForTree(tree1, treeOneLeaves)
    getLeafForTree(tree2, treeTwoLeaves)
    if treeOneLeaves == treeTwoLeaves:
        return True
    return False


def getLeafForTree(node, accumulator):
    if node:
        if isLeaf(node):
            accumulator.append(node.value)
            return
        getLeafForTree(node.left, accumulator)
        getLeafForTree(node.right, accumulator)


def isLeaf(node):
    return True if node and node.left is None and node.right is None else False
