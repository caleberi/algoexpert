def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


class Heap:
    def __init__(self, array, callback):
        self.heap = self.buildHeap(array)
        self.callback = callback
        self.length = len(self.heap)

    def buildHeap(self, array):
        firstParentIdx = (len(array)-2)//2
        for currentIdx in reversed(range(firstParentIdx+1)):
            self.siftDown(array, currentIdx, len(array)-1)
        return array

    def siftUp(self, heap, currentIdx):
        parentIdx = (currentIdx-1)//2
        while currentIdx >= 0:
            if  self.callback(heap, parentIdx, currentIdx):
                swap(heap, parentIdx, currentIdx)
                currentIdx = parentIdx
                parentIdx = (currentIdx-1)//2
            else:
                return

    def siftDown(self, heap, currentIdx, endIdx):
        childOneIdx = 2*currentIdx + 1
        while childOneIdx <= endIdx:
            childTwoIdx = 2*currentIdx+2 if currentIdx*2+2 <= endIdx else -1
            if childTwoIdx != -1 and self.callback(heap, childOneIdx, childTwoIdx):
                idxSwapIdx = childTwoIdx
            else:
                idxSwapIdx = childOneIdx
            if self.callback(heap, idxSwapIdx, currentIdx):
                swap(heap, idxSwapIdx, currentIdx)
                currentIdx = idxSwapIdx
                childOneIdx = 2*currentIdx + 1
            else:
                return

    def peek(self):
        return self.heap[0]

    def remove(self):
        swap(self.heap, 0, len(self.heap)-1)
        valueToRemove = self.heap.pop()
        self.length -= 1
        self.siftDown(self.heap, 0, len(self.heap)-1)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.siftUp(self.heap, len(self.heap)-1)

def MAX_HEAP(array,idxOne,idxTwo):
    return True if  array[idxOne] > array[idxTwo] else False

def MIN_HEAP(array,idxOne,idxTwo):
    return True if  array[idxOne] < array[idxTwo] else  False


