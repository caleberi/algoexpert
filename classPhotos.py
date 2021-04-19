def classPhotos(redShirtHeights, blueShirtHeights):
	tallestRed,shortestRed = getTallestStudentInRow(redShirtHeights)
	tallestBlue,shortestBlue = getTallestStudentInRow(blueShirtHeights)
	redAsFront=False
	if tallestRed>=tallestBlue and shortestRed>=shortestBlue:
		redAsFront=True
    redShirtHeights.sort()
	blueShirtHeights.sort()
	arrangement= zip(blueShirtHeights,redShirtHeights) if redAsFront else zip(redShirtHeights,blueShirtHeights)
	for col in arrangement:
		if col[0]>=col[1]:
			return False
    return True


def getTallestStudentInRow(row):
	return (max(row),min(row))
