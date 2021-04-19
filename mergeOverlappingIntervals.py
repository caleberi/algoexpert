def mergeOverlappingIntervals(intervals):
    intervals.sort()
    lastMergedIdx = None
    mergedCount = 0
    for i in range(1, len(intervals)):
        firstInterval = intervals[i-1]
        secondInterval = intervals[i]
        if secondInterval[0] <= firstInterval[1]:
            mergedInterval = [min(secondInterval[0], firstInterval[0]), max(
                secondInterval[1], firstInterval[1])]
            intervals = intervals[:i-1]+mergedInterval+intervals[i+1]
    return intervals
    # return [[]]


print(mergeOverlappingIntervals([
    [1, 2],
    [3, 5],
    [4, 7],
    [6, 8],
    [9, 10]
]))
print(mergeOverlappingIntervals([
    [20, 21],
    [22, 23],
    [0, 1],
    [3, 4],
    [23, 24],
    [25, 27],
    [5, 6],
    [7, 19]
]))


intervals = [
    [
        [20, 21],
        [22, 23],
        [0, 1],
        [3, 4],
        [23, 24],
        [25, 27],
        [5, 6],
        [7, 19]
    ],
    [
        [1, 22],
        [-20, 30]
    ],
    [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 1]
    ], [
        [43, 49],
        [9, 12],
        [12, 54],
        [45, 90],
        [91, 93]
    ], [
        [-5, -4],
        [-4, -3],
        [-3, -2],
        [-2, -1],
        [-1, 0]
    ], [
        [89, 90],
        [-10, 20],
        [-50, 0],
        [70, 90],
        [90, 91],
        [90, 95]
    ], [
        [1, 10],
        [10, 20],
        [20, 30],
        [30, 40],
        [40, 50],
        [50, 60],
        [60, 70],
        [70, 80],
        [80, 90],
        [90, 100]
    ]
]
