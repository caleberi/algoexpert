# def searchInSortedMatrix(matrix, target):
#     result = [-1, -1]
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == target:
#                 result[0] = i
#                 result[1] = j
#                 return result
#     return result


def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0])-1
    while col>= 0  and row <len(matrix):
        if matrix[row][col] > target:
            col-=1
        elif  matrix[row][col] < target:
            row+=1
        else:
            return [row,col]
    return [-1,-1]