def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def quickSort(array):
    startIdx = 0
    endIdx = len(array)-1
    quickSortHelper(array,startIdx,endIdx)
    return array

def quickSortHelper(array,startIdx,endIdx):
    if endIdx <= startIdx:
        return 
    pivotIdx=startIdx
    leftIdx=startIdx+1
    rightIdx=endIdx
    while leftIdx <= rightIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(array, leftIdx, rightIdx)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    swap(array, pivotIdx, rightIdx)
    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx-(rightIdx+1)
    if leftSubarrayIsSmaller :
        quickSortHelper(array,startIdx,rightIdx-1)
        quickSortHelper(array,rightIdx+1,endIdx)
    else:
        quickSortHelper(array,rightIdx+1,endIdx)
        quickSortHelper(array,startIdx,rightIdx-1)
    



print(quickSort([8,5,2,3,5,6,9]))
