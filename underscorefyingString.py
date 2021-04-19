def getLocations(string, substring):
    locations = []
    for i in range(0, len(string)):
        stidx = i
        edidx = i+len(substring)
        current = ''.join(string[stidx:edidx])
        if current == substring:
            locations.append([stidx, edidx])
    return locations


def collapseLocations(locations):
    if len(locations) == 0:
        return []
    collapseLocations = [locations[0]]
    for i in range(1, len(locations)):
        if locations[i][0] <= locations[i-1][1]:
            collapseLocations[-1][1] = locations[i][1]
            continue
        collapseLocations.append(locations[i])
    return collapseLocations


def underscorifySubstring(string, substring):
    locations = getLocations(string, substring)
    collapsedLocations = collapseLocations(locations)
    if  len(collapsedLocations)==0:
        return string
    tmp = list(string)
    for i in range(len(tmp)):
        if i < len(collapsedLocations):
            tmp.insert(collapsedLocations[i][0]+i, '_')
    for i in range(len(tmp)):
        if i < len(collapsedLocations):
            tmp.insert(collapsedLocations[i][1]+(i*2)+1, '_')
    return ''.join(tmp)

# # "_test_this is a _testtest_ to see if _testestest_ it works"
# # "testthis is a testtest to see if testestest it works"
# # [[0,3],[14,17],[18,21],[31,41]]


# def collapse(locations):
#     if not locations:
#         return locations
#     newLocations = [locations[0]]
#     previous = newLocations[0]
#     for i in range(1, len(locations)):
#         current = locations[i]
#         if current[0] <= previous[1]:
#             previous[1] = current[1]
#         else:
#             newLocations.append(current)
#             previous = current
#     return newLocations


# def getLocations(string: str, substring: str):
#     locations: list = []
#     startIdx: int = 0
#     while startIdx < len(string):
#         nextIdx: int = string.find(substring, startIdx)
#         if nextIdx != -1:
#             locations.append([nextIdx, nextIdx+len(substring)])
#             startIdx = nextIdx+1
#         else:
#             break
#     return locations

# def underscorify(string, locations):
#     locationsIdx = 0
#     stringIdx = 0
#     inBetweenUnderScores = False
#     finalChars = []
#     i = 0
#     while stringIdx < len(string) and locationsIdx < len(locations):
#         if stringIdx == locations[locationsIdx][i]:
#             finalChars.append("_")
#             inBetweenUnderScores = not inBetweenUnderScores
#             if not inBetweenUnderScores:
#                 locationsIdx += 1
#             i = 0 if i == 1 else 1
#         finalChars.append(string[stringIdx])
#         stringIdx += 1
#     if locationsIdx < len(locations):
#         finalChars.append('_')
#     elif stringIdx < len(string):
#         finalChars.append(string[stringIdx:])
#     return "".join(finalChars)


# def underscorifySubstring(string, substring):
#     locations = collapse(getLocations(string, substring))
#     return underscorify(string, locations)


print(underscorifySubstring(
    "testthis is a testtest to see if testestest it works", 'test'))
print(underscorifySubstring(
    "testthis is a testest to see if testestes it works", 'test'))
print(underscorifySubstring("testthis is a test to see if it works", 'test'))
print(underscorifySubstring("tttttttttttttatt", "tt"))
 