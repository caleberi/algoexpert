def largestRectangleUnderSkyline(buildings):
    if len(buildings)==0:
        return 0
    previousBuildingMaxArea=[(buildings[0]*1,buildings[0])]
    largestRectangleForward=previousBuildingMaxArea[0][0]
    for idx,building in enumerate(buildings):
        currentBuildingHeight=building
        minHeightBefore = previousBuildingMaxArea[-1][1]
        maxAreaBeforeCurrent = previousBuildingMaxArea[-1][0]
        currentBuildingArea = 1 * currentBuildingHeight
        currentBuildingPastArea = (idx+1)*min(minHeightBefore,currentBuildingHeight)
        largestCurrentRectangle=max(currentBuildingPastArea,currentBuildingArea,maxAreaBeforeCurrent)
        if largestCurrentRectangle > largestRectangleForward:
            largestRectangleForward=largestCurrentRectangle
        previousBuildingMaxArea.append((largestCurrentRectangle,min(minHeightBefore,currentBuildingHeight)))

    previousBuildingMaxArea=[(buildings[-1]*1,buildings[-1])]
    largestRectangleReverse=previousBuildingMaxArea[0][0]
    for idx,building in enumerate(reversed(buildings)):
        currentBuildingHeight=building
        minHeightBefore = previousBuildingMaxArea[-1][1]
        maxAreaBeforeCurrent = previousBuildingMaxArea[-1][0]
        currentBuildingArea = 1 * currentBuildingHeight
        currentBuildingPastArea = (idx+1)*min(minHeightBefore,currentBuildingHeight)
        largestCurrentRectangle=max(currentBuildingPastArea,currentBuildingArea,maxAreaBeforeCurrent)
        if largestCurrentRectangle > largestRectangleReverse:
            largestRectangleReverse=largestCurrentRectangle
        previousBuildingMaxArea.append((largestCurrentRectangle,min(minHeightBefore,currentBuildingHeight)))

    return max(largestRectangleReverse,largestRectangleForward)
