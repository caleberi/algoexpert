# def sameBSTs(arrayOne,arrayTwo):
#     if len(arrayOne) != len(arrayTwo):
#         return False
#     if len(arrayOne)== 0 and len(arrayTwo)==0:
#         return True
#     if arrayTwo[0]!=arrayOne[0]:
#         return False

#     leftOne = getSmaller(arrayOne)
#     leftTwo = getSmaller(arrayTwo)
#     rightOne =getBiggerOrEqual(arrayOne)
#     rightTwo = getBiggerOrEqual(arrayTwo)

#     return sameBSTs(leftOne,leftTwo) and sameBSTs(rightOne,rightTwo)


# def getSmaller(array):
#     smaller =[]
#     for i in range(1,len(array)):
#         if array[i] <array[0]:
#             smaller.append(array[i])
#     return smaller

# def getBiggerOrEqual(array):
#     bigger =[]
#     for i in range(1,len(array)):
#         if array[i] >= array[0]:
#             bigger.append(array[i])
#     return bigger


def sameBsts(arrayOne, arrayTwo):
    return areSameBsts(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))


def areSameBsts(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minVal, maxVal):
    if rootIdxOne == -1 or rootIdxTwo == -1:
        return rootIdxOne == rootIdxTwo

    if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
        return False

    leftRootIdxOne = getIdxOfFirstSmaller(arrayOne, rootIdxOne, minVal)
    leftRootIdxTwo = getIdxOfFirstSmaller(arrayTwo, rootIdxTwo, minVal)
    rightRootIdxOne = getIdxOfFirstBiggerOrEqual(arrayOne, rootIdxOne, maxVal)
    rightRootIdxTwo = getIdxOfFirstBiggerOrEqual(arrayTwo, rootIdxTwo, maxVal)

    currentValue = arrayOne[rootIdxOne]
    leftAreSame = areSameBsts(
        arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minVal, currentValue)
    rightAreSame = areSameBsts(
        arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, currentValue, maxVal)
    return leftAreSame and rightAreSame


def getIdxOfFirstSmaller(array, startingIdx, minVal):
    for i in range(startingIdx+1, len(array)):
        if array[i] < array[startingIdx] and array[i] >= minVal:
            return i
    return -1


def getIdxOfFirstBiggerOrEqual(array, startingIdx, maxVal):
    for i in range(startingIdx+1, len(array)):
        if array[i] >= array[startingIdx] and array[i] < maxVal:
            return i
    return -1


print(sameBSTs([10, 15, 8, 12, 94, 81, 5, 2, 11],
               [10, 8, 5, 15, 2, 12, 78, 11, 94, 81]))
