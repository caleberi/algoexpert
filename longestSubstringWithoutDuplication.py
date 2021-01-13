def longestSubstringWithoutDuplication(string):
    if len(string) == 0:
        return string
    lastSeen = {}
    longest = [0,1]
    startIdx=0
    for i,ch in enumerate(string):
        if ch  in lastSeen:
            startIdx=max(startIdx,lastSeen[ch]+1)
        if longest[1]-longest[0]<i+1-startIdx:
            longest = [startIdx,i+1]
        lastSeen[ch]=i
    return string[longest[0]:longest[1]]


print(longestSubstringWithoutDuplication("clementisacpa"))
print(longestSubstringWithoutDuplication("abc"))
print(longestSubstringWithoutDuplication("a"))
