def dijkstrasAlgorithm(start, edges):
    visited = set()
    numberOfVertices = len(edges)
    shortestPathSoFar = [float("inf")] * numberOfVertices
    shortestPathSoFar[start] = 0
    while len(visited) != numberOfVertices:
        vertex, currentMinDistance = getVertexMinDistance(
            shortestPathSoFar, visited)
        if currentMinDistance == float("inf"):
            break
        visited.add(vertex)
        for edge in edges[vertex]:
            destination, distanceToDestination = edge
            if destination in visited:
                continue
            newPathDistance = currentMinDistance+distanceToDestination
            currentDestinationDistance = shortestPathSoFar[destination]
            if newPathDistance <= currentDestinationDistance:
                shortestPathSoFar[destination] = newPathDistance

    return list(map(lambda x: -1 if x == float("inf") else x, shortestPathSoFar))


def getVertexMinDistance(distances, visited):
    currentMinDistance = float('inf')
    vertex = None
    for vertexIdx, distance in enumerate(distances):
        if vertexIdx in visited:
            continue
        if distance <= currentMinDistance:
            currentMinDistance = distance
            vertex = vertexIdx
    return [vertex, currentMinDistance]


answer = dijkstrasAlgorithm(0,
                   [[[1, 7]], [[2, 6], [3, 20], [4, 3]],
                       [[3, 14]], [[4, 2]], [], []]
                   )

print(answer)