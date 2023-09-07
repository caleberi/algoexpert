

from typing import List


def threeNumberSum(array:List[int],targeSum:int) -> List[List[int]] :
    array.sort()
    triplets = []
    for i in range(len(array)-2):
        left = i + 1
        right = len(array)-1
        while left < right:
            currentSum = array[left] + array[right] + array[i]
            if currentSum ==  targeSum:
                triplets.append([array[i],array[left], array[right]])
                right -= 1
                left += 1
            elif currentSum > targeSum:
                right -= 1
            elif currentSum < targeSum:
                left += 1
            
    return triplets