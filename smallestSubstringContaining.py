def smallestSubstringContaining(bigString, smallString):
    targetCharCounts = getCharCounts(smallString)
    substringBounds = getSubStringBounds(bigString, targetCharCounts)
    return getStringFromBounds(bigString, substringBounds)


def getSubStringBounds(string, targetCharCounts):
    subStringBounds = [0, float("inf")]
    subStringCharCounts = {}
    numUniqueChar = len(targetCharCounts.keys())
    numuniqueCharFound = 0
    leftPtr = 0
    rightPtr = 0
    while rightPtr < len(string):
        rightChar = string[rightPtr]
        if rightChar not in targetCharCounts:
            rightPtr += 1
            continue
        increaseCharCount(rightChar, subStringCharCounts)
        if subStringCharCounts[rightChar] == targetCharCounts[rightChar]:
            numuniqueCharFound += 1
        while numuniqueCharFound == numUniqueChar and leftPtr <= rightPtr:
            subStringBounds = getCloserBounds(
                leftPtr, rightPtr, subStringBounds[0], subStringBounds[1])
            leftChar = string[leftPtr]
            if leftChar not in targetCharCounts:
                leftPtr += 1
                continue
            if subStringCharCounts[leftChar] == targetCharCounts[leftChar]:
                numuniqueCharFound -= 1
            decreaseCharCount(leftChar, subStringCharCounts)
            leftPtr += 1
        rightPtr += 1
    return subStringBounds


def getCloserBounds(idx1, idx2, idx3, idx4):
    return [idx1, idx2] if idx2-idx1 < idx4-idx3 else [idx3, idx4]


def getStringFromBounds(string, bounds):
    start, end = bounds
    if end == float("inf"):
        return ""
    return string[start:end+1]


def getCharCounts(string):
    charCounts = {}
    for char in string:
        increaseCharCount(char, charCounts)
    return charCounts


def increaseCharCount(char, charCounts):
    if char not in charCounts:
        charCounts[char] = 0
    charCounts[char] += 1


def decreaseCharCount(char, charCount):
    charCount[char] -= 1
