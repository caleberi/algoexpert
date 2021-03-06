class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


O(N) | O(N)


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


O(K+h) | O(h)


def findKthLargestValueInBst(tree, k):
    vector = []
    findKthLargestValueInBstHelper(tree, vector, k)
    return vector[k-1]


def findKthLargestValueInBstHelper(tree, v, k):
    if len(v) > k:
        return
    if tree.left is None and tree.right is None:
        v.append(tree.value)
        return
    if tree.right is not None:
        findKthLargestValueInBstHelper(tree.right, v, k)
    v.append(tree.value)
    if tree.left is not None:
        findKthLargestValueInBstHelper(tree.left, v, k)


def findKthLargestValueInBst(tree, k):
    pass
