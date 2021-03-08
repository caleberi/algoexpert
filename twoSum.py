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
