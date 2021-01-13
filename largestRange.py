def largestRange(array): # [1,11,3,0,15,2,4,10,7,12,6]
    bestPossibleRange = []
    history={} #{1:False,11:False,.....6:False}
    longestLengthSoFar=0
    for element in array:
        history[element]=True
    
    for num in array :
        if not history[num]:
            continue
        history[num]=False
        currentLength=1
        leftPossibleNumber=num-1
        rightPossibleNumber=num+1
        while leftPossibleNumber in history:
            history[leftPossibleNumber]=False
            currentLength +=1
            leftPossibleNumber-=1
        while rightPossibleNumber in history:
            history[rightPossibleNumber]=False
            currentLength+=1
            rightPossibleNumber+=1
        
        if currentLength > longestLengthSoFar:
            bestPossibleRange=[leftPossibleNumber+1,rightPossibleNumber-1]
            longestLengthSoFar=currentLength
    return bestPossibleRange

print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))




 