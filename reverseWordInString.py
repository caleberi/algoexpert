def reverseWordsInString(string):
    # Write your code here.
    tokens = generateTokens(string)
    return ''.join(reverseToken(tokens))


def generateTokens(string, sep=" "):
    current = ""
    ret = []
    for ch in string:
        if ch == sep and current != "":
            ret.append(current)
            current = ""
        if ch == sep and current == "":
            ret.append(ch)
            continue

        current += ch
    if current != "":
        ret.append(current)
    return ret


def reverseToken(tokens):
    leftIdx = 0
    rightIdx = len(tokens)-1
    while leftIdx <= rightIdx:
        swap(leftIdx, rightIdx, tokens)
        leftIdx += 1
        rightIdx -= 1
    return tokens


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]
