# def searchForRange(array, target):
#     history = {}
#     for i in range(len(array)-1):
#         if array[i] not in history:
#             history[array[i]] = [i]
#         else:
#             history[array[i]].append(i)

#     if len(history[target]) == 0:
#         return [-1, -1]
#     else:
#         return [history[target][0], history[target][len(history[target])-1]]


# def searchForRange(array, target):
#     finalRange = [-1, -1]
#     alteredBinarySearchRange(array, target, 0, len(array)-1, finalRange, True)
#     alteredBinarySearchRange(array, target, 0, len(array)-1, finalRange, False)
#     return finalRange


# def alteredBinarySearchRange(array, target, left, right, finalRange, goLeft):
#     if right < left:
#         return

#     mid = (left+right)//2
#     if array[mid] < target:
#         alteredBinarySearchRange(array, target, mid+1,
#                                  right, finalRange, goLeft)
#     elif array[mid] > target:
#         alteredBinarySearchRange(
#             array, target, left, mid-1, finalRange, goLeft)
#     else:
#         if goLeft:
#             if mid == 0 or array[mid-1] != target:
#                 finalRange[0] = mid
#             else:
#                 alteredBinarySearchRange(
#                     array, target, left, mid-1, finalRange, goLeft)
#         else:
#             if mid == len(array)-1 or array[mid+1] != target:
#                 finalRange[1] = mid
#             else:
#                 alteredBinarySearchRange(
#                     array, target, mid+1, right, finalRange, goLeft)


#     return finalRange


def searchForRange(array, target):
    finalRange = [-1, -1]
    alteredBinarySearchRange(array, target, 0, len(array)-1, finalRange, True)
    alteredBinarySearchRange(array, target, 0, len(array)-1, finalRange, False)
    return finalRange


def alteredBinarySearchRange(array, target, left, right, finalRange, goLeft):
    while left <= right:
        mid = (left+right)//2
        if array[mid] < target:
            left = mid+1
        elif array[mid] > target:
            right = mid-1
        else:
            if goLeft:
                if mid == 0 or array[mid-1] != target:
                    finalRange[0] = mid
                    return
                else:
                    right = mid-1
            else:
                if mid == len(array)-1 or array[mid+1] != target:
                    finalRange[1] = mid
                    return
                else:
                    left = mid+1

    return finalRange


print(
    searchForRange(
        [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45
    )
)
