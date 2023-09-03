from typing import List


def twoNumberSum(array, targetSum):
    hashMap = {}
    for idx in range(len(array)):
        currentNum = array[idx]
        difference = targetSum-currentNum
        if difference not in hashMap and currentNum not in hashMap:
            hashMap[difference] = currentNum
        else:
            return [currentNum, hashMap[currentNum]]
    return []


def twoNumberSumV2(array, targetSum):
    for idx in range(len(array)-1):
        firstNum = array[idx]
        for idx2 in range(idx+1,len(array)):
            secondNum = array[idx2]
            if secondNum + firstNum  == targetSum :
                return [firstNum, secondNum]
            
    return []


def twoNumberSumV4(array:List[int], targetSum:int)->List[int]:
    leftPointer = 0
    rightPointer = len(array) - 1
    
    array.sort()
    while leftPointer < rightPointer:
        currentSum = array[leftPointer] + array[rightPointer]
        if currentSum > targetSum :
            rightPointer -= 1
        elif currentSum < targetSum :
            leftPointer += 1
        else :
            return [array[leftPointer], array[rightPointer]]
    return  []
