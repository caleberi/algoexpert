def swapNode(tree):
    tree.right, tree.left = tree.left, tree.right


def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        currentNode = queue.pop(0)
        if currentNode is None:
            continue
        swapNode(currentNode)
        queue.append(currentNode.left)
        queue.append(currentNode.right)


def invertBinaryTreeRecursive(tree):
    if tree is None:
        return
    swapNode(tree)
    invertBinaryTreeRecursive(tree.left)
    invertBinaryTreeRecursive(tree.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
