# def indexEqualsValue(array):
#     indexArray = [i for i in range(len(array))]
#     for i in range(len(array)):
#             if array[i] == indexArray[i]:
#                 return i
#     return -1


# def indexEqualsValue(array):
#     return indexEqualsValueHelper(array, 0, len(array)-1)


# def indexEqualsValueHelper(array, leftIdx, rightIdx):
#     while leftIdx <= rightIdx:
#         middleIdx = leftIdx + (rightIdx-leftIdx)//2
#         middleValue = array[middleIdx]
#         if middleValue == middleIdx and middleIdx==0 :
#             return middleIdx
#         elif middleValue < middleIdx:
#             leftIdx = middleIdx+1
#         elif middleValue == middleIdx  and array[middleIdx-1]<middleIdx-1:
#             return middleIdx
#         else:
#             rightIdx = middleIdx-1
#     return -1


def indexEqualsValue(array):
    return indexEqualsValueHelper(array, 0, len(array)-1)


def indexEqualsValueHelper(array, leftIdx, rightIdx):
    if leftIdx > rightIdx:
        return -1
    middleIdx = leftIdx + (rightIdx-leftIdx)//2
    middleValue = array[middleIdx]
    
    if middleValue < middleIdx:
        return indexEqualsValueHelper(array, middleIdx+1, rightIdx)
    elif middleValue == middleIdx and middleIdx == 0:
        return middleIdx
    elif middleValue == middleIdx and array[middleIdx-1] < middleIdx-1:
        return middleIdx
    else:
        return indexEqualsValueHelper(array, leftIdx, middleIdx-1)


print(indexEqualsValue([-2, 0, 2, 4, 6, 8, 10]))
