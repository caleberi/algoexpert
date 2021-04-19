
class ContinuousMedianHandler:
    def __init__(self):
        self.lowers = Heap(MAX_HEAP_FUNC, [])
        self.greaters = Heap(MIN_HEAP_FUNC, [])
        self.median = None

    def insert(self, number):
        if not self.lowers.length or number < self.lowers.peek():
            self.lowers.insert(number)
        else:
            self.greaters.insert(number)
        self.rebalanceHeaps()
        self.updateMedian()

    def rebalanceHeaps(self):
        if self.lowers.length-self.greaters.length == 2:
            self.greaters.insert(self.lowers.remove())
        elif self.greaters.length-self.lowers.length == 2:
            self.lower.insert(self.greaters.remove())
        else:
            return

    def updateMedian(self):
        if self.lowers.length == self.greaters.length:
            self.median = (self.lowers.peek()+self.greaters.peek())/2
        elif self.lowers.length > self.greaters.length:
            self.median = self.lowers.peek()
        else:
            self.median = self.greaters.peek()

    def getMedian(self):
        return self.median


class Heap:
    def __init__(self, array, compareFunc):
        self.compareFunc = compareFunc
        self.heap = self.buildHeap(array)
        self.length = len(self.heap)

    def buildHeap(self, array):
        firstParentIdx = (len(array)-2)//2
        for currentIdx in reversed(range(firstParentIdx+1)):
            self.siftDown(currentIdx, len(array)-1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = (currentIdx*2)+1
        while childOneIdx <= endIdx:
            childTwoIdx = (2*currentIdx+2) if 2 * currentIdx + 2 <= endIdx else -1
            if childTwoIdx != -1:
                if(self.compareFunc(heap[childOneIdx], heap[childTwoIdx])) and childTwoIdx != -1:
                    idxToSwap = childTwoIdx
                else:
                    idxToSwap = childOneIdx
            else:
                idxToSwap = childOneIdx
            if self.compareFunc(heap[currentIdx], heap[idxToSwap]):
                self.swap(idxToSwap, currentIdx, heap)
                currentIdx = idxToSwap
                childOneIdx = (currentIdx*2)+1
            else:
                return

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx-1)//2
        while currentIdx > 0:
            if self.compareFunc(heap[currentIdx], heap[parentIdx]):
                self.swap(parentIdx, currentIdx, heap)
                currentIdx = parentIdx
                parentIdx = (currentIdx-1)//2
            else:
                return

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, self.length-1, self.heap)
        valueToRemove = self.heap.pop()
        self.length -= 1
        self.siftDown(0, self.length-1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.siftUp(self.length-1, self.heap)

    def swap(self, i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]


def MAX_HEAP_FUNC(a, b):
    return a > b


def MIN_HEAP_FUNC(a, b):
    return a < b
