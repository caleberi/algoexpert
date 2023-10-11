def moveElementToEnd(array, toMove):
    i,j = 0 , len(array)-1
    while i < j:
        if array[j] == toMove and array[i] == toMove:
            j -= 1
        elif  (array[j] != toMove and array[i] == toMove):
            array[j],array[i] = array[i],array[j]
            j -= 1
            i += 1
        else:
            i += 1     
    return array