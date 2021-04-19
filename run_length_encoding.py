# def runLengthEncoding(string):
#     history = {}
#     result = ""
#     for i in range(len(string)):
#         if string[i] not in history and len(history.keys()) != 0:
#             for k, v in history.items():
#                 result += str(v)+k
#             history.clear()
#         if string[i] not in history:
#             history[string[i]] = 1
#         else:
#             if string[i] in history and history[string[i]] < 9:
#                 history[string[i]] += 1
#             elif string[i] in history and history[string[i]] == 9:
#                 result += str(history[string[i]])+string[i]
#                 history[string[i]] = 1
#         if i >= len(string)-1:
#             for k, v in history.items():
#                 result += str(v)+k
#     return result

def runLengthEncoding(string):
    encodedStringsCharacters = []
    currentRunLength = 1
    for i in range(1, len(string)):
        previousCharacter = string[i-1]
        currentCharacter = string[i]
        if currentCharacter != previousCharacter or currentRunLength == 9:
            encodedStringsCharacters.append(str(currentRunLength))
            encodedStringsCharacters.append(previousCharacter)
            currentRunLength = 0
        currentRunLength += 1

    encodedStringsCharacters.append(str(currentRunLength))
    encodedStringsCharacters.append(string[len(string)-1])
    return "".join(encodedStringsCharacters)
