def shiftedBinarySearch(array, target):
    return modifiedBinarySearch(array, target, 0, len(array)-1)


def modifiedBinarySearch(array, target, firstIdx, lastIdx):
    if lastIdx < firstIdx:
        return -1
    middle = (firstIdx+lastIdx)//2
    potentialMatch = array[middle]
    leftNum = array[firstIdx]
    rightNum = array[lastIdx]
    if potentialMatch == target:
        return middle
    elif leftNum <= potentialMatch:
        if target < potentialMatch and target >=leftNum:
            return modifiedBinarySearch(array, target, firstIdx, middle-1)
        else:
            return modifiedBinarySearch(array, target, middle+1, lastIdx)
    else:
        if target > potentialMatch and  target<=rightNum:
            return modifiedBinarySearch(array, target, middle+1, lastIdx)
        else:
            return modifiedBinarySearch(array, target, firstIdx, middle-1)


def shiftedBinarySearchIterative(array, target):
    return modifiedBinarySearchIterative(array, target,0,len(array)-1)

def modifiedBinarySearchIterative(array,target,left,right):
    while left <= right:
        middle = (left+right)//2
        potentialMatch = array[middle]
        leftNum = array[left]
        rightNum = array[right]
        if potentialMatch == target:
            return middle
        elif leftNum <= potentialMatch:
            if target < potentialMatch and target >=leftNum:
               right= middle-1
            else:
                left = middle+1
        else:
            if target > potentialMatch and  target<=rightNum:
                 left = middle+1
            else:
                right= middle-1
    return -1


print(shiftedBinarySearchIterative([45,61, 71, 72, 73, 100,-5,0, 1,20, 21,28, 33, 37], 28))
