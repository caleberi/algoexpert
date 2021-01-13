def siftDown(heap, currentIdx, endIdx):
    childOneIdx = 2*currentIdx + 1
    while childOneIdx <= endIdx:
        childTwoIdx = 2*currentIdx+2 if currentIdx*2+2 <= endIdx else -1
        if childTwoIdx != -1 and MAX_HEAP(heap, childTwoIdx,childOneIdx):
            idxSwapIdx = childTwoIdx
        else:
            idxSwapIdx = childOneIdx
        if MAX_HEAP(heap, idxSwapIdx, currentIdx):
            swap(heap, idxSwapIdx, currentIdx)
            currentIdx = idxSwapIdx
            childOneIdx = 2*currentIdx + 1
        else:
            return


def buildMaxHeap(array):
    firstParentIdx = (len(array)-1)//2
    for currentIdx in reversed(range(firstParentIdx+1)):
        siftDown(array, currentIdx, len(array)-1)
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def MAX_HEAP(array, idxOne, idxTwo):
    return True if array[idxOne] > array[idxTwo] else False


def heapSort(array):
    buildMaxHeap(array)
    for endIdx in reversed(range(1, len(array))):
        swap(array, 0, endIdx)
        siftDown(array, 0, endIdx-1)
	return array