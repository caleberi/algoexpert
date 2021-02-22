class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    vector = []
    findKthLargestValueInBstHelper(tree, vector)
    return vector[k-1]


def findKthLargestValueInBstHelper(tree, v):
    if tree.left is None and tree.right is None:
        v.append(tree.value)
        return
    if tree.right is not None:
        findKthLargestValueInBstHelper(tree.right, v)
    v.append(tree.value)
    if tree.left is not None:
        findKthLargestValueInBstHelper(tree.left, v)
