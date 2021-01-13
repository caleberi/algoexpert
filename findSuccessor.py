# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# def findSuccessor(tree, node):
#     visited = []
#     findSuccessorHelper(tree, node, visited)
#     for i in range(len(visited)):
#         if visited[i] == node:
#             return visited[i+1]
#     return None


# def findSuccessorHelper(tree, node, visited):
#     if tree is None:
#         return None
#     findSuccessorHelper(tree.left, node, visited)
#     visited.append(tree)
#     findSuccessorHelper(tree.right, node, visited)

def findSuccessor(tree, node):
    if node.right is not None:
        return getLeftMostChild(node.right)
    return getRightMostParent(node)

def getLeftMostChild(node):
    current = node
    while  current.left is not  None:
        current=current.left
    return current

def getRightMostParent(node):
    current = node
    while current.parent is not None and current.parent.right == current:
        current=current.parent
    return current.parent
