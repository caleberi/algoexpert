def firstNonRepeatingCharacter(string):
    visited = set()
    nonRepeatedTable = {}
    for i in range(len(string)):
        ch = string[i]
        if ch not in nonRepeatedTable and ch not in visited:
            nonRepeatedTable[ch] = i
            visited.add(ch)
        elif ch in nonRepeatedTable and ch in visited:
            del nonRepeatedTable[ch]
    firstIdx = 10000
    for _, val in nonRepeatedTable.items():
        if val < firstIdx:
            firstIdx = val
    return -1 if firstIdx == 10000 else firstIdx
