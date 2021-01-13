def isImportant(token):
    return len(token)>0 and token != "."

def shortenPath(path):
    # tokenize the string  breaking down the path by  splitting with "/"
    # create a stack  and  push to it using the following conditions
    startwithSlash = path[0]=="/"
    tokens = filter(isImportant,path.split("/"))
    stack=[]
    if startwithSlash :
        stack.append("")
    for token in tokens:
        if token == "..":
            if len(stack) == 0 or  stack[-1]=="..":
                stack.append(token)
            elif stack[-1] != "":
                _ = stack.pop()
        else:
            stack.append(token)

    if len(stack)==1 and stack[0] == "":
        return "/"
    return "/".join(stack)
    


print(shortenPath("foo/../.."))
print(shortenPath("/../../../this////one/./../../is/../../going/../../to/be/./././../../../just/a/forward/slash/../../../../../../foo"))
print(shortenPath("../../foo/../../bar/baz"))
print(shortenPath("/foo/./././bar/./baz///////////test/../../../kappa"))
print(shortenPath("/foo/../test/../test/../foo//bar/./baz"))
print(shortenPath("/../../.."))
print(shortenPath('/foo/bar/baz/././.'))
print(shortenPath("/foo/../test/../test/../foo//bar/./baz"))
print(shortenPath("/foo//test/./test/./foo//bar///./baz"))
print(shortenPath("/foo/../test/../test/../foo//bar/./baz"))
print(shortenPath("/../test/../../foo//bar/./baz"))
print(shortenPath("/foo/../test/../test/foo//bar/./baz"))
print(shortenPath("/foo/../test/../foo//bar/./baz"))
