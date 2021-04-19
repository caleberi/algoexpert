UP, DOWN, LEFT, RIGHT = 'up', 'down', 'right', 'left'


def rectangleMania(coords):
    coordsTable = getCoordsTable(coords)
    return getRectangleCount(coords, coordsTable)


def getCoordsTable(coords):
    coordsTable = {}
    for coord1 in coords:
        coord1Directions = {
            UP: [], DOWN: [], RIGHT: [], LEFT: []
        }
        for coord2 in coords:
            coord2Direction = getCoordsDirection(coord1, coord2)
            if coord2Direction in coord1Directions:
                coord1Directions[coord2Direction].append(coord2)
        coord1String = coordToString(coord1)
        coordsTable[coord1String] = coord1Directions
    return coordsTable


def getCoordsDirection(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    if y2 == y1:
        if x2 > x1:
            return RIGHT
        else:
            return LEFT
    elif x2 == x1:
        if y2 > y1:
            return UP
        else:
            return DOWN
    return ""


def coordToString(coord):
    x, y = coord
    return str(x) + '-' + str(y)


def getRectangleCount(coords, coordsTable):
    rectangleCount = 0
    for coord in coords:
        rectangleCount += clockwiseCountRectangles(
            coord, coordsTable, UP, coord)
    return rectangleCount


def clockwiseCountRectangles(coord, coordsTable, direction, origin):
    if direction == LEFT:
        rectangleFound = origin in coordsTable[coordToString][LEFT]
        return 1 if rectangleFound else 0
    else:
        rectangleCount = 0
        nextDirection = getNextClockwiseCount(direction)
        for nextCoord in coordsTable[coordToString][direction]:
            rectangleCount += clockwiseCountRectangles(
                nextCoord, coordsTable, nextDirection, origin)
        return rectangleCount


def getNextClockwiseCount(direction):
    if direction == UP:
        return RIGHT
    if direction == RIGHT:
        return DOWN
    if direction == DOWN:
        return LEFT
    return ''
