def isOutOfBounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width


def zigzagTraverse(array):
    height = len(array)-1
    width = len(array[0])-1
    result = []
    row, col = 0, 0
    goingDown = True
    goingRight = False
    # how do we make decision based on choices below :
    # moving down [row+=1][col]
    # moving right [row][col+=1]
    # moving diagonally upright [row-=1][col+=1]
    # moving diagonally downleft [col-=1][row-=1]
    """
        -
    [1,3,4, 10]
     | / / / |
    [2,5,9, 11]  ==> [1,2,3,4]
     /  /  /
    [6,8,12,15] 
     | / /  /|
    [7,13,14,16]
         _
    """
    while not isOutOfBounds(row, col, height, width):
        result.append(array[row][col])
        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1

    return result


array = [
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16]
]
print(zigzagTraverse(array))
