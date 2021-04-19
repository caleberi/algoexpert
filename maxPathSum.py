class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class NodeSumInfo:
    def __init__(self, maxBranchSum, runningPathSum):
        self.maxBranchSum = maxBranchSum
        self.runningPathSum = runningPathSum


def maxPathSum(tree):
    result = maxPathSumHelper(tree)
    return result.runningPathSum


def maxPathSumHelper(tree):
    if tree is None:
        return NodeSumInfo(0, float("-inf"))
    leftReturnCall = maxPathSumHelper(tree.left)
    rightReturnCall = maxPathSumHelper(tree.right)
    leftMaxSumAsBranch, leftMaxPathSum = leftReturnCall.maxBranchSum, leftReturnCall.runningPathSum
    rightMaxSumAsBranch, rightMaxPathSum = rightReturnCall.maxBranchSum, rightReturnCall.runningPathSum
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)
    value = tree.value
    maxSumAsBranch = max(maxChildSumAsBranch+value, value)
    maxSumAsTreeSum = max(leftMaxSumAsBranch+value +
                          rightMaxSumAsBranch, maxSumAsBranch)

    maxPathSum = max(leftMaxPathSum,
                     rightMaxPathSum, maxSumAsTreeSum)
    return NodeSumInfo(maxSumAsBranch,  maxPathSum)
