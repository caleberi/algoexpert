def patternMatcher(pattern, string):
    if len(pattern) > len(string):
        return []
    newPattern = getNewPattern(pattern)
    didSwitch = newPattern[0] != pattern[0]
    counts = {"x": 0, "y": 0}
    firstYPos = getCountAndFirstYPos(newPattern, counts)
    if counts["y"] != 0:
        for lenOfX in range(1,len(string)):
            lenOfY = (len(string)-counts["x"]*lenOfX)/counts["y"]
            if lenOfY <= 0 or lenOfY % 1 != 0:
                continue
            lenOfY = int(lenOfY)
            yIdx = firstYPos*lenOfX
            x = string[:lenOfX]
            y = string[yIdx:yIdx+lenOfY]
            potentialMatch = map(lambda char: x if char ==
                                 "x" else y, newPattern)
            if "".join(potentialMatch) == string:
                return [x, y] if not didSwitch else [y, x]
    else:
        lenOfX = len(string)/counts["x"]
        if lenOfX % 1 == 0:
            lenOfX = int(lenOfX)
            x = string[:lenOfX]
            potentialMatch = map(lambda char: x, newPattern)
            if "".join(potentialMatch) == string:
                return [x, ""] if not didSwitch else ["", x]
    return []


def getNewPattern(pattern) -> list:
    patternLetters = list(pattern)
    if patternLetters[0] == "x":
        return patternLetters
    else:
        return ["x" if ch == "y" else "y" for ch in patternLetters]


def getCountAndFirstYPos(pattern, counts):
    firstYpos = None
    for idx, ch in enumerate(pattern):
        counts[ch] += 1
        if ch == "y" and firstYpos is None:
            firstYpos = idx
    return firstYpos
