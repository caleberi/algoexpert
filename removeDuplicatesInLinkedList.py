# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # current node assumed not to have a duplicate
    current = linkedList  # pointer on the list head
    while current:
        if current.next and current.value == current.next.value:
            currentNextNode = current.next
            newNextNode = current.next.next
            if newNextNode:
                current.next = newNextNode
                currentNextNode.next = None
            else:
                current.next = None
        current = current if current.next and current.next.value == current.value else current.next

    return linkedList
