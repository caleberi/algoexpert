class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeNodePathInfo:
    def __init__(self,diameter,height):
        self.height = height
        self.diameter = diameter


def binaryTreeDiameter(tree):
    return binaryTreeDiameterHelper(tree).diameter

def binaryTreeDiameterHelper(tree):
    if tree is None:
        return TreeNodePathInfo(0,0)
    leftTreeData = binaryTreeDiameterHelper(tree.left)
    rightTreeData = binaryTreeDiameterHelper(tree.right)
    
    longestPathThroughRoot = leftTreeData.height + rightTreeData.height
    maxDiameterSoFar = max(leftTreeData.diameter,rightTreeData.diameter)
    currentDiameter = max(longestPathThroughRoot,maxDiameterSoFar)
    currentHeight = 1+max(leftTreeData.height,rightTreeData.height)

    return  TreeNodePathInfo(currentDiameter,currentHeight)