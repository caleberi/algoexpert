def waterfallStreams(array, source):
    rowAbove = array[0][:]
    rowAbove[source] = -1
    for row in range(1, len(array)):
        currentRow = array[row][:]
        for idx in range(len(rowAbove)):
            valueAbove = rowAbove[idx]
            hasWaterAbove = valueAbove < 0
            hasBlock = currentRow[idx] == 1
            if not hasWaterAbove:
                continue
            if not hasBlock:
                currentRow[idx] += valueAbove
                continue
            splitWater = valueAbove/2
            rightIdx = idx
            while rightIdx+1 < len(rowAbove):
                rightIdx += 1
                if rowAbove[rightIdx] == 1:
                    break
                if currentRow[rightIdx] != 1:
                    currentRow[rightIdx] += splitWater
                    break
            leftIdx = idx
            while leftIdx-1 >= 0:
                leftIdx -= 1
                if rowAbove[leftIdx] == 1:
                    break
                if currentRow[leftIdx] != 1:
                    currentRow[leftIdx] += splitWater
                    break
        rowAbove = currentRow
    finalPercentages = list(map(lambda num: num*-100, rowAbove))
    return finalPercentages
