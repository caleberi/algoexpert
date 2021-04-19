def longestBalancedSubstring(string):
    stack = []
    maxBalancedLengthSoFar = 0
    numberOfOpeningParentheses = 0
    currentLength = 0
    store =[]
    numberOfClosingParentheses = 0
    for i in range(len(string)):
        if string[i] == ')':
            if len(stack) > 0:
                top = stack[-1]
                if top == "(":
                    numberOfClosingParentheses += 1
                    numberOfOpeningParentheses += 1
                    currentLength += 2
                    _ = stack.pop()
            else:
                currentLength = 0
                numberOfClosingParentheses = 0
                numberOfOpeningParentheses = 0
                continue
        elif string[i] == '(':
            stack.append('(')
        else:
            pass
        store.append(currentLength)
        if currentLength > maxBalancedLengthSoFar and numberOfClosingParentheses == numberOfOpeningParentheses:
            maxBalancedLengthSoFar = currentLength

        stk=[]
        maxBalancedLengthSoFar = 0
        numberOfOpeningParentheses = 0
        currentLength = 0
        for i in reversed(range(len(string))):
            if string[i] == ')':
                if len(stack) > 0:
                    top = stack[-1]
                    if top == "(":
                        numberOfClosingParentheses += 1
                        numberOfOpeningParentheses += 1
                        currentLength += 2
                        _ = stack.pop()
                else:
                    currentLength = 0
                    numberOfClosingParentheses = 0
                    numberOfOpeningParentheses = 0
                    continue
            elif string[i] == ')':
                stack.append(')')
            else:
                pass
            if currentLength > maxBalancedLengthSoFar and numberOfClosingParentheses == numberOfOpeningParentheses:
                maxBalancedLengthSoFar = currentLength
    return maxBalancedLengthSoFar

print(longestBalancedSubstring("((()(())))))((()))(("))
print(longestBalancedSubstring("(()(()"))
print(longestBalancedSubstring("())))))())(((())((()"))
print(longestBalancedSubstring("())))))())(((())((()"))
print(longestBalancedSubstring("(()))("))

