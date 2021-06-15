# from pprint import PrettyPrinter
# from os import open
# temp = open('./output.txt')
# printer = PrettyPrinter(4,40,2,temp)
def BFS(map,i,j):
    visited = {}
    count=0
    count+=findPath(map,i,j,visited)
    return count;


def isVisited(visited,location):
    return location in visited
def isBlocked(map,i,j):
    return map[i][j]==1
def isOutOfBounds(map,i,j):
    return i <0 or i>len(map)-1 or j<0 or j>len(map[i])-1

def findPath(map,i,j,visited):
    location=str(i)+" -> "+str(j)
    if isVisited(visited,location):
        return 0
    if isOutOfBounds(map, i, j):
        return 0
    if isBlocked(map, i, j):
        return 0
    if i==len(map)-1 and j==len(map[0])-1:
        return 1
    visited[location]=[i,j]
    map[i][j]=1
    neighbours=getNeigbours(map,i,j)
    count=0
    for neighbour in neighbours:
        x=neighbour[0]
        y=neighbour[1]
        ret = findPath(map, x, y, visited)
        if ret!=0:
            count+=ret
    # printer.pprint(map)
    map[i][j]=0
    visited.pop(location)
    return count

def getNeigbours(map,i,j):
    neighbour=[]
    if i <0 or i>len(map)-1 or j<0 or j>len(map[i])-1:
        return neighbour
    validMoves = [[i+1,j],[i,j+1]]
    for moves in validMoves:
        x=moves[0]
        y=moves[1]
        if i < 0 or i >len(map)-1 or j<0 or j>len(map[i])-1:
            continue
        neighbour.append(moves)
    return neighbour

print(BFS(
[
    [0,0,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [1,0,0,0]
],
0,0
))

print(
BFS(
[
    [0,0,0,0],
    [0,1,0,0],
    [0,0,0,0],
    [0,0,1,0],
    [0,0,0,0]
],0,0
)
)

print(BFS(
[
    [0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],
    [1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],
    [0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],
    [0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],
    [1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
    [0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
    [0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],
    [0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],
    [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],
    [0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],
    [1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],
    [1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],
    [1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]
]
,0,0
))
