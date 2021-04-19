class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree: BinaryTree):
    return heightBalancedBinaryTreeHelper(tree)[1]


def heightBalancedBinaryTreeHelper(tree: BinaryTree) -> tuple:
    if tree is None:
        return (-1, True)
    leftHeight, leftHeightBalanceStatus = heightBalancedBinaryTreeHelper(
        tree.left)
    rightHeight, rightHeightBalanceStatus = heightBalancedBinaryTreeHelper(
        tree.right)
    heightDifferenceStatus = (leftHeightBalanceStatus and rightHeightBalanceStatus and abs(
        leftHeight-rightHeight) <= 1)
    height = max(leftHeight, rightHeight)+1
    return (height, heightDifferenceStatus)
