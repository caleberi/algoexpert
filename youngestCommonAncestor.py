# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    return getYoungestCommonAncestorHelper(topAncestor, descendantOne, descendantTwo)


def getYoungestCommonAncestorHelper(topAncestor, descendantOne, descendantTwo):
    depthOfDescendantOne = findDepthOfAncestralTree(descendantOne)
    depthOfDescendantTwo = findDepthOfAncestralTree(descendantTwo)
    if depthOfDescendantOne > depthOfDescendantTwo:
        possibleAncestorAtLevel = traverseUntilDepthdiff(
            descendantOne, getAbsDiffOfDepth(depthOfDescendantOne, depthOfDescendantTwo))
        return grabAncestor(possibleAncestorAtLevel, descendantTwo)
    else:
        possibleAncestorAtLevel = traverseUntilDepthdiff(
            descendantTwo, getAbsDiffOfDepth(depthOfDescendantOne, depthOfDescendantTwo))
        return grabAncestor(possibleAncestorAtLevel, descendantOne)


def grabAncestor(descendantOne, descendantTwo):
    if descendantOne is not descendantTwo:
        return grabAncestor(descendantOne.ancestor, descendantTwo.ancestor)
    return descendantOne


def traverseUntilDepthdiff(tree: AncestralTree, diff, currentLevel=0):
    if diff == currentLevel:
        return tree
    return traverseUntilDepthdiff(tree.ancestor, diff, currentLevel+1)


def getAbsDiffOfDepth(x, y):
    return abs(x-y)


def findDepthOfAncestralTree(tree, depth=0):
    # if we still have an ancestor move forward else return depth of tree
    if tree.ancestor is not None:
        return findDepthOfAncestralTree(tree.ancestor, depth+1)
    else:
        return depth


# class AncestralTree:
#     def __init__(self, name):
#         self.name = name
#         self.ancestor = None


# def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
#     depthOfDescendantOne = findDepthOfAncestralTree(descendantOne)
#     depthOfDescendantTwo = findDepthOfAncestralTree(descendantTwo)
#     if depthOfDescendantOne > depthOfDescendantTwo:
#         return backtrackAncestralTree(descendantOne, descendantTwo, depthOfDescendantOne-depthOfDescendantTwo)
#     else:
#         return backtrackAncestralTree(descendantTwo, descendantOne, depthOfDescendantTwo-depthOfDescendantOne)


# def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
#     while diff > 0:
#         lowerDescendant = lowerDescendant.ancestor
#         diff -= 1
#     while lowerDescendant != higherDescendant:
#         lowerDescendant = lowerDescendant.ancestor
#         higherDescendant = higherDescendant.ancestor
#     return lowerDescendant


# def findDepthOfAncestralTree(tree, depth=0):
#     # if we still have an ancestor move forward else return depth of tree
#     if tree.ancestor is not None:
#         return findDepthOfAncestralTree(tree.ancestor, depth+1)
#     else:
#         return depth
