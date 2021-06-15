class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def searchForAncestor(node, possibleAncestor, nodeToParents):
    if node.value not in nodeToParents or nodeToParents[node.value] is None:
        return
    if node.value in nodeToParents and nodeToParents[node.value] == possibleAncestor:
        return nodeToParents[node.value]
    return searchForAncestor(nodeToParents[node.value], possibleAncestor, nodeToParents)


def populateNodeToParents(node, nodeToParents, parent=None):
    if node:
        nodeToParents[node.value] = parent
        populateNodeToParents(node.left, nodeToParents, node)
        populateNodeToParents(node.right, nodeToParents, node)


def searchForDescendant(node, nodeOne, nodeThree):
    if node is None:
        return
    if node.value == nodeOne.value:
        return node
    if node.value == nodeThree.value:
        return node
    leftSearch = searchForDescendant(node.left, nodeOne, nodeThree)
    rightSearch = searchForDescendant(node.right, nodeOne, nodeThree)
    if leftSearch is not None and rightSearch is not None and leftSearch != rightSearch:
        return None
    if leftSearch and rightSearch is None:
        return leftSearch
    if rightSearch and leftSearch is None:
        return rightSearch
        return None


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    descendant = searchForDescendant(nodeTwo, nodeOne, nodeThree)
    if descendant is None:
        return False
    if descendant.value == nodeOne.value:
        possibleAncestor = nodeThree
    if descendant.value == nodeThree.value:
        possibleAncestor = nodeOne
    nodeToParents = {}
    if possibleAncestor is nodeOne:
        populateNodeToParents(nodeOne, nodeToParents)
    if possibleAncestor is nodeThree:
        populateNodeToParents(nodeThree, nodeToParents)
    ancestor = searchForAncestor(nodeTwo, possibleAncestor, nodeToParents)
    if ancestor == possibleAncestor:
        return True
    return False
