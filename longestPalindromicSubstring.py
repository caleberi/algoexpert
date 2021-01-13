def isPalindromic(string):
    left = 0
    right = len(string)-1
    while left <= right:
        if string[left] != string[right]:
            return False
        left+=1
        right-=1
    return True

# O(N^3)time | O(1) space
def longestPalindromicSubstring(string):
    currentLongestSubstring = ""
    slow = 0
    while slow < len(string):
        fast = slow
        while fast < len(string):
            currentString = string[slow:fast+1]
            print(currentString)
            if isPalindromic(currentString) and len(currentLongestSubstring) <= len(currentString):
                currentLongestSubstring = currentString
            fast += 1
        slow += 1
    return currentLongestSubstring

# O(N^2) time | O(1) space
def longestPalindromicSubstring(string):
    currentLongest=[0,1]
    for i in range(1,len(string)):
        odd=getLongestPalindromeFrom(string,i-1,i+1)
        even=getLongestPalindromeFrom(string,i-1,i)
        longest =max(odd,even,key=lambda x: x[1]-x[0])
        currentLongest=max(longest,currentLongest,key=lambda x: x[1]-x[0])
    
    return string[currentLongest[0]:currentLongest[1]]

def getLongestPalindromeFrom(string,leftIdx,rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx-=1
        rightIdx+=1
    return [leftIdx+1,rightIdx]

print(longestPalindromicSubstring("abaxyzzyxf"))
