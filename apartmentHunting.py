# def apartmentHunting(blocks, reqs):
#     maxDistanceAtBlock = [float("-inf") for block in blocks]
#     for i in range(len(blocks)):
#         for req in reqs:
#             closestReqDistance = float("inf")
#             for j in range(len(blocks)):
#                 if blocks[j][req]:
#                     closestReqDistance = min(
#                         closestReqDistance, distanceBetween(i, j))
#             maxDistanceAtBlock[i] = max(
#                 maxDistanceAtBlock[i], closestReqDistance)
#     return getIdxAtMinValue(maxDistanceAtBlock)


# def distanceBetween(a, b):
#     return abs(a-b)


# def getIdxAtMinValue(array):
#     idxAtMinValue = 0
#     minValue = float("inf")
#     for i in range(len(array)):
#         currentValue = array[i]
#         if currentValue < minValue:
#             minValue = currentValue
#             idxAtMinValue = i
#     return idxAtMinValue


def apartmentHunting(blocks, reqs):
    minDistancesFromBlocks = list(
        map(lambda req: getMinDistances(blocks, req), reqs))
    maxDistancesFromBlocks = getMaxDistancesAtBlocks(
        blocks, minDistancesFromBlocks)
    return getIdxAtMinValue(maxDistancesFromBlocks)


def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
    maxDistancesFromBlocks = [0 for block in blocks]
    for i in range(len(blocks)):
        minDistancesFromBlock = list(map(lambda distances: distances[i], minDistancesFromBlocks))
        maxDistancesFromBlocks[i] = max(minDistancesFromBlock)
    return maxDistancesFromBlocks


def getMinDistances(blocks, req):
    minDistances = [0 for block in blocks]
    closestReqIdx = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = distanceBetween(i, closestReqIdx)
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = min(
            minDistances[i], distanceBetween(i, closestReqIdx))
    return minDistances


def getIdxAtMinValue(array):
    idxAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMinValue = i
    return idxAtMinValue


def distanceBetween(a, b):
    return abs(a-b)


blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True}
]

reqs = ["gym", "school", "store"]
print(apartmentHunting(blocks, reqs))
