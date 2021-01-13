class Building:
    def __init__(self, height, idx):
        self.height = height
        self.idx = idx


def sunsetViews(buildings, direction):
    if len(buildings) == 0:
        return []
    if direction == "EAST":
        stk = [Building(buildings[0], 0)]
        for idx in range(1, len(buildings)):
            currentBuildingHeight = buildings[idx]
            if currentBuildingHeight >= stk[-1].height:
                while len(stk) > 0 and currentBuildingHeight >= stk[-1].height:
                    stk.pop()
                stk.append(Building(currentBuildingHeight, idx))
            else:
                stk.append(Building(currentBuildingHeight, idx))
        return [b.idx for b in stk]
    else:
        stk = [Building(buildings[-1], len(buildings)-1)]
        for idx in reversed(range(len(buildings)-1)):
            currentBuildingHeight = buildings[idx]
            if currentBuildingHeight >= stk[-1].height:
                while len(stk) > 0 and currentBuildingHeight >= stk[-1].height:
                    stk.pop()
                stk.append(Building(currentBuildingHeight, idx))
            else:
                stk.append(Building(currentBuildingHeight, idx))
        temp = [b.idx for b in stk]
        temp.sort()
        return temp
