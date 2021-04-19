# def sortStack(stack):
#     return sort(stack)
# def sort(stack):
#     if len(stack)==0 or len(stack)==1:
#         return stack
#     top=stack.pop()
#     sort(stack) # ([4,1]) c=3, ([4]) c=1  , ([]) c=4 r=NAN [4]
#     if len(stack)==0 :
#         stack.append(top)
#         return
#     insert(stack,top)
# 	return stack
#
# def insert(stack,value):
#     if len(stack)==0 or stack[-1]<value:
#         stack.append(value)
#         return
#     top=stack.pop()
#     insert(stack, value)
#     stack.append(top)


def sortStack(stack):
    if len(stack)==0:
        return stack
    top = stack.pop()
    sortStack(stack)
    insertInSortedOrder(stack,top)
    return stack

def insertInSortedOrder(stack,value):
    if len(stack)==0 or stack[-1]<=value:
        stack.append(value)
        return
    top=stack.pop()
    insertInSortedOrder(stack, value)
    stack.append(top)
