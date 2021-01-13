# O(N^(N/2)) time | O(N) space
# def rightSmallerThan(array):
#     if len(array)==0:
#         return []
#     result = []
#     for i in range(len(array)):
#         count=0
#         current = array[i]
#         left = i+1
#         right = len(array)-1
#         while right>=left:
#             if left==right :
#                 if current > array[left] and current > array[right]:
#                     count+=1
#                     left+=1
#                     right-=1
#                     continue
#             if current > array[left]:
#                 count+=1
#             if current > array[right]:
#                 count+=1
#             left+=1
#             right-=1
#         result.append(count)
#     return result

# O(N^2) | O(N)
def rightSmallerThan(array):
    if len(array) == 0:
        return []

    result = []
    for i in range(len(array)):
        count = 0
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                count += 1
        result.append(count)
    return result


class SpecialBST:
    def __init__(self, value, idx, numSmallerAtInsertTime) -> None:
        self.value = value
        self.idx = idx
        self.left = None
        self.right = None
        self.numSmallerAtInsertTime= numSmallerAtInsertTime
        self.leftSubTreeSize=0

    def insert(self, val, idx,  numSmallerAtInsertTime):
        if self.value < val:
            numSmallerAtInsertTime+=self.leftSubTreeSize
            if val > self.value:
                numSmallerAtInsertTime+=1
            if self.right is None:
                self.right = SpecialBST(val,idx,numSmallerAtInsertTime)
            else:
                self.right.insert(val,idx,numSmallerAtInsertTime)
        else:
            self.leftSubTreeSize += 1
            if self.left is None:
                self.left = SpecialBST(val,idx,numSmallerAtInsertTime)
            else:
                self.left.insert(val, idx, numSmallerAtInsertTime)


def rightSmallerThan(array):
    if len(array) == 0:
        return []
    lastIdx = len(array)-1
    bst = SpecialBST(array[lastIdx], lastIdx, 0)
    for idx in reversed(range(len(array)-1)):
        bst.insert(array[idx], idx, 0)

    rightSmallerCounts = array[:]
    getRightSmallerCounts(bst, rightSmallerCounts)
    return rightSmallerCounts


def getRightSmallerCounts(bst, rightSmallerCounts):
    if bst is None:
        return
    rightSmallerCounts[bst.idx] = bst.numSmallerAtInsertTime
    getRightSmallerCounts(bst.left, rightSmallerCounts)
    getRightSmallerCounts(bst.right, rightSmallerCounts)


"""
        8
       / \
     5    11
     /
    -1
       \
       3
    /   \
    2    4 
"""
print(rightSmallerThan([8, 5, 11, -1, 3, 4, 2]))
# print(rightSmallerThan([9, 8, 10, 11, 12, 13]))
