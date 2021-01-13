# def numberOfBinaryTreeTopologies(n):
#     if n == 0:
#         return 1
#     numberOfTrees =0
#     for leftTreeSize in range(0,n):
#         rightTreeSize = n - 1 - leftTreeSize
#         numberOfTreeLeft = numberOfBinaryTreeTopologies(leftTreeSize)
#         numberOfTreeRight = numberOfBinaryTreeTopologies(rightTreeSize)
#         numberOfTrees+=numberOfTreeLeft*numberOfTreeRight
#     return numberOfTrees


# def numberOfBinaryTreeTopologies(n,cache={0:1}):
#     if n in cache:
#         return cache[n]
#     numberOfTrees =0
#     for leftTreeSize in range(0,n):
#         rightTreeSize = n - 1 - leftTreeSize
#         numberOfTreeLeft = numberOfBinaryTreeTopologies(leftTreeSize,cache)
#         numberOfTreeRight = numberOfBinaryTreeTopologies(rightTreeSize,cache)
#         numberOfTrees+=numberOfTreeLeft*numberOfTreeRight
#     cache[n]=numberOfTrees
#     return numberOfTrees

def numberOfBinaryTreeTopologies(n):
    cache = [1]
    for m in range(1, n+1):
        numberOfTrees = 0
        for leftTreeSize in range(m):
            rightTreeSize = m-1-leftTreeSize
            numberOfLeftTrees = cache[leftTreeSize]
            numberOfRightTrees = cache[rightTreeSize]
            numberOfTrees += numberOfLeftTrees * numberOfRightTrees
        cache.append(
            numberOfTrees
        )
    return cache[n]


print(numberOfBinaryTreeTopologies(3))
