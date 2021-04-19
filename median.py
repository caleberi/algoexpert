def median(arr1,arr2):
    result=[]
    merged = merger(0,0,arr1,arr2,result)
    idx=(len(merged)-1)//2
    if len(merged)%2:
        return merged[idx]
    return (merged[idx]+merged[idx+1])/2.0
    


#O(2*N+M)
def merger(p1,p2,arr1,arr2,result):
    print(f'merger(p1:{p1},p2:{p2},arr1:{arr1},arr2:{arr2},result:{result})')
    if p1 == len(arr1) or p2 == len(arr2):
        if p2 < len(arr2):
            result.append(arr2[p2])
            return merger(p1,p2+1,arr1,arr2,result)
        if p1 < len(arr1):
            result.append(arr1[p1])
            return merger(p1+1,p2,arr1,arr2,result)
        return result
    if arr1[p1]<arr2[p2]:
        result.append(arr1[p1])
        return merger(p1+1,p2,arr1,arr2,result)
    else:
        result.append(arr2[p2])
        return merger(p1,p2+1,arr1,arr2,result)

print(median([1,3,5],[2,4,6]))