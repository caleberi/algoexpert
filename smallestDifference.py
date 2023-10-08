def smallestDifference(arrayOne, arrayTwo):
    if not len(arrayOne) and len(arrayTwo):
        return []
    arrayOne.sort()
    arrayTwo.sort()
    ret , diff = [],float("inf")
    i ,j = 0,0 
    while i < len(arrayOne) and j < len(arrayTwo):
        currentDiff =  abs(arrayOne[i]-arrayTwo[j])
        if currentDiff < diff :
            ret = [arrayOne[i],arrayTwo[j]]
            diff = min(currentDiff ,diff)
        if arrayOne[i] < arrayTwo[j] :
            i += 1
        else:
            j += 1
    return ret
    