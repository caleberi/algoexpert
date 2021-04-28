def cycleInGraph(edges):
    for vertex, edge in enumerate(edges):
        visited = {}
        queue = [vertex]
        while queue:
            currentVertex = queue.pop(0)
            if currentVertex in visited:
                return True
            visited[currentVertex] = True
            if len(edges[currentVertex]) == 0 and len(queue) > 0:
                queue.pop(0)
            for connectedVertex in edges[currentVertex]:
                queue.append(connectedVertex)
    return False


################################################################
# for every vertex in  graph
#   d = getalledges of current vertex
#   e = current vertex edge
#   add them to the queue
#   for each one of the connected vertex
#       get a connected node closer
#       unless the node has  not been visited continue
#       else return True
################################################################

edges = [
    [1, 3], [2, 3, 4], [0], [], [2, 5], []
]

print(cycleInGraph(
    edges
))

edges = [
    [1, 2],
    [2],
    []
]
print(cycleInGraph(
    edges
))
