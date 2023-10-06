def isValidSubsequence(array, sequence):
    m,n =  len(sequence),len(array)
    if m > n:
        return False
    sPtr,aPtr = 0, 0
    while aPtr  < n:
        if sPtr < m:
            if sequence[sPtr] == array[aPtr] :
                sPtr += 1
        aPtr += 1
    return sPtr == m