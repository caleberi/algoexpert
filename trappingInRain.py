def trappingInRain(array):
    totalTrappedWater=0
    for i in range(1,len(array)-1): #because the first and last index will not have left and right max
        #{3,0,2,4} =>min{3,4}-arr[i]
        leftMax=findLeftMax(array,i)
        rightMax=findRightMax(array,i)
        totalTrappedWater += min(leftMax,rightMax)-array[i]
    return abs(totalTrappedWater)

def findLeftMax(array,pos):
    return max(list(array[:pos+1]))

def findRightMax(array,pos):
    return max(list(array[pos:]))

print(trappingInRain([3,0,2,0,4,9,0,4,8,9]))