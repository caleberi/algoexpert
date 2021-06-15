def longestBalancedParenthesisSubstring(string):
    if len(string) == 0:
        return 0

    stack = []
    maxlongestSubStrSoFar = 0
    longestSubStrSoFar = 0
    for ch in string:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if len(stack) != 0 and stack[-1] == "(":
                _ = stack.pop()
                longestSubStrSoFar += 2
                if longestSubStrSoFar > maxlongestSubStrSoFar:
                    maxlongestSubStrSoFar = max(
                        longestSubStrSoFar, maxlongestSubStrSoFar)
            else:
                if longestSubStrSoFar > maxlongestSubStrSoFar:
                    maxlongestSubStrSoFar = max(
                        longestSubStrSoFar, maxlongestSubStrSoFar)
                longestSubStrSoFar = 0
    if len(stack) != 0:
        stack = []
        rmaxlongestSubStrSoFar = 0
        longestSubStrSoFar = 0
        for ch in string:
            if ch == ")":
                stack.append(ch)
            elif ch == "(":
                if len(stack) != 0 and stack[-1] == ")":
                    _ = stack.pop()
                    longestSubStrSoFar += 2
                    if longestSubStrSoFar > rmaxlongestSubStrSoFar:
                        maxlongestSubStrSoFar = max(
                            longestSubStrSoFar, rmaxlongestSubStrSoFar)
                else:
                    if longestSubStrSoFar > rmaxlongestSubStrSoFar:
                        rmaxlongestSubStrSoFar = max(
                            longestSubStrSoFar, rmaxlongestSubStrSoFar)
                    longestSubStrSoFar = 0
        return max(rmaxlongestSubStrSoFar, maxlongestSubStrSoFar)
    return maxlongestSubStrSoFar


print(longestBalancedParenthesisSubstring("())(())"))
print(longestBalancedParenthesisSubstring(")(()))))((((()"))
print(longestBalancedParenthesisSubstring('()((())(())') == 4)
print(longestBalancedParenthesisSubstring('(()())'))
