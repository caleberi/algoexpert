# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def getParentsForEachNode(node, nodesToParents, parent=None):
    if node:
        nodesToParents[node.value] = parent
        getParentsForEachNode(node.left, nodesToParents, node)
        getParentsForEachNode(node.right, nodesToParents, node)


def getNodeFromValue(value, tree, nodesToParents):
    if tree.value == value:
        return tree
    nodeParent = nodesToParents[value]
    if nodeParent.left and nodeParent.left.value == value:
        return nodeParent.left
    return nodeParent.right


def findNodesDistanceK(tree, target, k):
    nodesToParents = {}
    getParentsForEachNode(tree, nodesToParents)
    targetNode = getNodeFromValue(target, tree, nodesToParents)
    queue = [(targetNode, 0)]
    seen = {targetNode.value}
    while len(queue) > 0:
        currentNode, distance = queue.pop(0)
        if distance == k:
            nodes = [node.value for node, _ in queue]
            nodes.append(currentNode.value)
            return nodes
        connectedNodes = [currentNode.left, currentNode.right,
                          nodesToParents[currentNode.value]]
        for node in connectedNodes:
            if node is None:
                continue
            if node.value in seen:
                continue
            seen.add(node.value)
            queue.append((node, distance+1))
        return []


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    # Write your code here.
    return []
