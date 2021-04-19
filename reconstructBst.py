# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, val):
        if val < self.value:
            if self.left is None:
                self.left = BST(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BST(val)
            else:
                self.right.insert(val)


def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return None
    root = BST(preOrderTraversalValues[0])
    for idx in range(1, len(preOrderTraversalValues)):
        val = preOrderTraversalValues[idx]
        root.insert(val)
    return root
