def allKindsOfNodeDepths(root):
    if root is None:
        return 0
    return allKindsOfNodeDepths(root.left)+allKindsOfNodeDepths(root.right)+nodeDepth(root)


def nodeDepth(tree, depth=0):
    if tree is None:
        return 0
    return nodeDepth(tree.left, depth+1)+nodeDepth(tree.right, depth+1)+depth


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
