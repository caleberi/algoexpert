from typing import List


def fourNumberSum(array:List[int],targetSum:int)->List[List[int]]:
    allPairSums  = {} # tracking the number of two sum pairs
    quadruplets = [] # return all quadrplets possible
    for i in range (1,len(array)-1):
        # try to find the first partial sum of the  target sum 
        # and index +  1 -- len(array) before computing the possible partial sum of the 
        # other aspect of the the target sum
        for j in range(i+1,len(array)):
            currentSum = array[i] +  array[j]
            difference =  targetSum - currentSum
            if difference  in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair + [array[j],array[i]]) 
        for k in range(0,i):
            currentSum = array[k] + array[i]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [array[k],array[i]]
            else:
                allPairSums[currentSum].append([array[k],array[i]])
    return quadruplets


def fourNumberSum(array:List[int],targetSum:int)->List[List[int]]:
    result = []
    array.sort()
    for i in range(len(array)-3):
        for j in range(i+1,len(array)-2):
            left = j+1
            right = len(array)-1
            while left < right:
                total_sum  =  array[left] + array[right] + array[i] + array[j]
                if total_sum == targetSum:
                    result.append([array[i], array[j], array[left], array[right]])
                    left += 1
                    right -=1
                elif total_sum > targetSum:
                    right -= 1
                else:
                    left += 1
    return result
