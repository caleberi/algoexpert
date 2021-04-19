# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def getLinkedListLength(head):
    count = 1
    while head is not None:
        count += 1
        head = head.next
    return count


def getMiddleNode(node, length):
    count = 1
    while count != length:
        count += 1
        node = node.next
    return node


def reverseLinkedList(node):
    prevNode = None
    currentNode = node
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = nextNode
    return prevNode


def linkedListPalindrome(head):
    length = getLinkedListLength(head)
    startNode = head
    middleEndNode = getMiddleNode(head, length//2)
    middleStartNode = reverseLinkedList(middleEndNode)
    middleEndNode.next = None
    while startNode is not None and middleStartNode is not None:
        if startNode.value != middleStartNode.value:
            return False
        startNode = startNode.next
        middleStartNode = middleStartNode.next
    return True


def linkedListPalindromePointer(head):
    slowNode = head
    fastNode = head
    while fastNode is not None and fastNode.next is not None:
        slowNode = slowNode.next
        fastNode = fastNode.next.next

    slowNode = reverseLinkedList(slowNode)
    while fastNode is not None and slowNode is not None:
        if fastNode.value != slowNode.value:
            return False
        slowNode = slowNode.next
        fastNode = fastNode.next
    return True


def linkedListRecursive(head):
    isPalindromeResults = isPalindrome(head,head)

def isPalindrome(leftNode,rightNode):
    if rightNode is None:
        return LinkedListInfo(True,leftNode)
    recursiveCallResults = isPalindrome(leftNode,rightNode.next)
    leftNodeToCompare = recursiveCallResults.leftNodeToCompare
    outerNodeAreEqual = recursiveCallResults.outerNodeAreEqual
    recursiveIsEqual = outerNodeAreEqual and  leftNodeToCompare.value == rightNode.value
    nextMatchingLeftNode = leftNodeToCompare.next

    return LinkedListInfo(recursiveIsEqual,nextMatchingLeftNode)
class  LinkedListInfo:
    def  __init__(self,outerNodeAreEqual,leftNodeToCompare):
        self.outerNodeAreEqual = outerNodeAreEqual
        self.leftNodeToCompare = leftNodeToCompare