def globMatching(fileName, pattern):
    locations = getLocationOfSymbols(pattern)
    for pos in locations:
        if pattern[pos]=="*":
            stringBefore=fileName[len(fileName)-pos]

def getLocationOfSymbols(pattern):
    return [idx for idx in range(len(pattern)) if pattern[idx] == "*" or pattern[idx] == "?"]
