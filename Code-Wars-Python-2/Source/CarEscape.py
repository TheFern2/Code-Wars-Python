def escape(carpark):
    hasStart = False
    ladderPosition = 0
    currentPosition = 0
    goingDownStr = ""
    goingDownStartingLevel = 0

    out = []
    targetIndex = 0
    isBottomLevel = False
    ladderFound = False
    goingDown = False
    targetFirst = False
    moveCount = 0

    for i in range(len(carpark)):
        if 2 in carpark[i]:
            targetIndex = carpark[i].index(2)
        if 1 in carpark[i]:
            targetIndex = carpark[i].index(1)
        elif i == len(carpark):
            isBottomLevel = True
            targetIndex = len(carpark)-1
        elif 2 not in carpark[i] and not hasStart:
            continue
        for j in range(len(carpark[i])):
            hasStart = True
            # 0 and ladder not found
            if carpark[i][j] == 0 and not ladderFound:
                continue
            # 0 and ladder found OR 0 and targetFirst or targetIndex and not targetFirst
            elif carpark[i][j] == 0 and ladderFound or carpark[i][j] == 0 and targetFirst or targetIndex == j:
                moveCount += 1
                if moveCount == 1 and targetIndex == j:
                    goingDown = True
                    goingDownStartingLevel = i
                    break
                if goingDown and targetIndex == j:
                    moveCount += 1
                if goingDown and targetIndex != j:
                    goingDownStr = "D%d" % moveCount
                    moveCount = 0
            elif carpark[i][j] == 1 and not ladderFound:
                ladderFound = True
                ladderPosition = j
                if targetFirst:
                    moveCount += 1
                    break
            elif targetIndex and not ladderFound:
                targetFirst = True
        if not goingDown:
            if ladderPosition < targetIndex:
                out.append("L%d" % moveCount)
            elif ladderPosition > targetIndex:
                out.append("R%d" % moveCount)
            moveCount = 0
        if goingDown and goingDownStartingLevel != i:
            if ladderPosition < targetIndex:
                out.extend(goingDownStr, "L%d" % moveCount)
            elif ladderPosition > targetIndex:
                out.extend(goingDownStr, "R%d" % moveCount)
            goingDown = False
        currentPosition = ladderPosition
        # reset variables
        targetFirst = False
        ladderFound = False


def escape2(carpark):
    foundStart = False
    currentIndex = 0
    targetIndex = 0
    downCount = 0
    out = []

    for i in range(len(carpark)):
        if 2 not in carpark[i] and not foundStart:
            continue
        if 2 in carpark[i] and i == len(carpark)-1:
            currentIndex = carpark[i].index(2)
            targetIndex   = len(carpark[i])-1
            if currentIndex == targetIndex:
                break
            else:
                if currentIndex > targetIndex:
                    out.append("L%d" % abs(((targetIndex + 1) - (currentIndex + 1))))
                elif currentIndex < targetIndex:
                    out.append("R%d" % abs(((targetIndex + 1) - (currentIndex + 1))))
                break
        # level with start
        if 2 in carpark[i]:
            currentIndex = carpark[i].index(1)
            targetIndex   = carpark[i].index(2)
            foundStart = True

            if currentIndex > targetIndex:
                out.append("R%d" % abs(((targetIndex + 1) - (currentIndex + 1))))
            elif currentIndex < targetIndex:
                out.append("L%d" % abs(((targetIndex + 1) - (currentIndex + 1))))
            downCount += 1

        # middle levels
        elif 1 in carpark[i] and 2 not in carpark[i] and foundStart:
            targetIndex   = carpark[i].index(1)

            if currentIndex > targetIndex:
                if downCount > 0:
                    out.extend(["D%d" % downCount, "L%d" % abs((targetIndex + 1) - (currentIndex + 1))])
                    downCount = 1 #test
                else:
                    out.append("L%d" % abs(((targetIndex + 1) - (currentIndex + 1))))
                    downCount += 1
            elif currentIndex < targetIndex:
                if downCount > 0:
                    out.extend(["D%d" % downCount, "R%d" % abs((targetIndex + 1) - (currentIndex + 1))])
                    downCount = 1 #test
                else:
                    out.append("R%d" % abs(((targetIndex + 1) - (currentIndex + 1))))
                    downCount += 1
            elif currentIndex == targetIndex:
                downCount += 1
            currentIndex = targetIndex

        # bottom level
        elif 1 not in carpark[i] and foundStart:
            targetIndex = len(carpark[i])-1

            if currentIndex > targetIndex:
                if downCount > 0:
                    out.extend(["D%d" % downCount, "L%d" % abs((targetIndex + 1) - (currentIndex + 1))])
                else:
                    out.append("L%d" % abs(((targetIndex + 1) - (currentIndex + 1))))
                    downCount += 1
            elif currentIndex < targetIndex:
                if downCount > 0:
                    out.extend(["D%d" % downCount, "R%d" % abs((targetIndex + 1) - (currentIndex + 1))])
                else:
                    out.append("R%d" % abs(((targetIndex + 1) - (currentIndex + 1))))
                    downCount += 1
            elif currentIndex == targetIndex:
                out.append("D%d" % downCount)

    return out

def escape3(carpark):

    while 2 not in carpark[0]: carpark.pop(0)
    r, ground, pos = [], len(carpark) - 1, carpark[0].index(2)
    for f, floor in enumerate(carpark):
        stairs = floor.index(1) if f != ground else len(floor) - 1
        if stairs != pos:
            r, pos = r + ['RL'[stairs < pos] + str(abs(pos - stairs))], stairs
        if f != ground:
            r += [('D' + str(int(r.pop()[1:]) +1)) if 'D' in r[-1] else 'D1']
    return r

def escape4(carpark):
    floor, car = next((floor, car)
                      for floor, f in enumerate(carpark)
                      for car, c in enumerate(f) if c == 2)
    route, carpark[-1][-1] = [], 1
    while floor < len(carpark) - 1 or carpark[floor][car] != 1:
        start = floor, car
        while floor < len(carpark) - 1 and carpark[floor][car] == 1:
            floor += 1
        if floor > start[0]: route.append('D%d' % (floor - start[0]))
        car = carpark[floor].index(1)
        if car > start[1]: route.append('R%d' % (car - start[1]))
        if car < start[1]: route.append('L%d' % (start[1] - car))
    return route