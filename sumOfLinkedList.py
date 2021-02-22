# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne: LinkedList, linkedListTwo: LinkedList) -> LinkedList:
    if linkedListOne is None and linkedListTwo is not None:
        return linkedListTwo
    if linkedListTwo is None and linkedListOne is not None:
        return linkedListOne
    if linkedListTwo is None and linkedListOne is None:
        return LinkedList(0)
    carry = None
    result = None
    pResult = None
    while linkedListOne and linkedListTwo:
        digitSum = (linkedListOne.value + linkedListTwo.value +
                    carry) if carry else (linkedListOne.value+linkedListTwo.value)
        carry = digitSum//10 if digitSum >= 10 else None
        digitSum = digitSum % 10 if digitSum >= 10 else digitSum
        if result is None:
            result = LinkedList(digitSum)
            pResult = result
        else:
            pResult.next = LinkedList(digitSum)
            pResult = pResult.next
        linkedListOne = linkedListOne.next
        linkedListTwo = linkedListTwo.next

    if carry and linkedListOne is None and linkedListTwo is None:
        pResult.next = LinkedList(carry)

    if linkedListOne is not None and linkedListTwo is None:
        if carry:
            while carry and linkedListOne:
                digitSum = (linkedListOne.value+carry)
                carry = digitSum//10 if digitSum >= 10 else None
                digitSum = digitSum % 10 if digitSum >= 10 else digitSum
                if carry:
                    result = LinkedList(carry)
                else:
                    pResult.next = LinkedList(digitSum)
                    pResult = pResult.next
                linkedListOne = linkedListOne.next
        while linkedListOne:
            pResult.next = LinkedList(linkedListOne.value)
            pResult = pResult.next
            linkedListOne = linkedListOne.next
        else:
            while linkedListOne:
                pResult.next = LinkedList(linkedListOne.value)
                pResult = pResult.next
                linkedListOne = linkedListOne.next

    if linkedListTwo is not None and linkedListOne is None:
        if carry:
            while carry and linkedListTwo:
                digitSum = (linkedListTwo.value+carry)
                carry = digitSum//10 if digitSum >= 10 else None
                digitSum = digitSum % 10 if digitSum >= 10 else digitSum
                if carry:
                    result = LinkedList(carry)
                else:
                    pResult.next = LinkedList(digitSum)
                    pResult = pResult.next
                linkedListTwo = linkedListTwo.next
            while linkedListTwo:
                pResult.next = LinkedList(linkedListTwo.value)
                pResult = pResult.next
                linkedListTwo = linkedListTwo.next

        else:
            while linkedListTwo:
                pResult.next = LinkedList(linkedListTwo.value)
                pResult = pResult.next
                linkedListTwo = linkedListTwo.next

    return result
