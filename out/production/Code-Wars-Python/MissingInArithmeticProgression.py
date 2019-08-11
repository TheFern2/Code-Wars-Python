def find_missing(sequence):

    if len(sequence) <= 100:
        print(sequence)
    print("Sequence length",len(sequence))
    print(sequence[0], sequence[1], sequence[2], sequence[len(sequence) -1])

    progression = 0
    currentProgression = 0
    isNegative = [False] * len(sequence)
    isAllNegative = False
    isAllPositive = False
    negativeCount = 0
    positiveCount = 0
    expected = 0
    goingDown = False
    goingUp = False
    # check if numbers are negative
    for i in range(len(sequence)):
        if sequence[i] > 0:
            isNegative[i] = False
        elif sequence[i] < 0:
            isNegative[i] = True
    #print(isNegative)

    # check if all neg or pos
    for i in range(len(isNegative)):
        if not isNegative[i]:
            positiveCount += 1
        if isNegative[i]:
            negativeCount += 1

    if positiveCount == len(sequence):
        isAllPositive = True
    if negativeCount == len(sequence):
        isAllNegative = True

    # Would only apply if mixed negative and positive numbers
    if sequence[0] < sequence[len(sequence)-1]:
        goingUp = True
        print("Sequence going up")
    else:
        goingDown = True
        print("Sequence going down")

    # find progression
    for i in range(0, len(sequence)-1):
        # Have rules here based on two digits
        # If -3, 4 = 7 OR 4, -7 =
        if isNegative[i] and not isNegative[i+1] or not isNegative[i] and isNegative[i+1]:
            currentProgression = (sequence[i]) + (sequence[i+1])

            if goingDown and not isNegative[i] and isNegative[i+1]:
                currentProgression = (sequence[i] * -1) + (sequence[i+1])
            if goingUp and isNegative[i] and not isNegative[i+1]:
                currentProgression = (sequence[i] * -1) + (sequence[i+1])

            if progression == 0:
                progression = abs(currentProgression)
        # If 4, 7 = 3
        if not isNegative[i] and not isNegative[i+1]:
            currentProgression = (sequence[i+1]) - (sequence[i])
            if progression == 0:
                progression = abs(currentProgression)

        if isAllNegative or isAllPositive:
            currentProgression = abs(sequence[i+1]) - abs(sequence[i])
            if progression == 0:
                progression = abs(currentProgression)
        if currentProgression < progression:
            progression = currentProgression

    print("Progression", progression)

    # Would only apply if mixed negative and positive numbers
    if sequence[0] < sequence[len(sequence)-1]:
        goingUp = True
        print("Sequence going up")
    else:
        goingDown = True
        print("Sequence going down")

    # find missing number
    # TODO check if expected is negative or positive
    # by checking before and after numbers loop -2
    for i in range(len(sequence)-1):
        # BUG Rules need to be based on whether sequence is going up or going down
        # Example: 12, 4, -4 -> Going down
        # Example: 1, 2, 3   -> Going up
        if isAllPositive:
            expected = sequence[i] + progression
        if isAllNegative:
            expected = sequence[i] - progression
        if isNegative[i] and not isAllNegative:
            expected = sequence[i] - progression #last change of sign
            if goingDown:
                expected = sequence[i] + progression
            if goingUp:
                expected = sequence[i] + progression
        if not isNegative[i] and not isAllPositive:
            expected = sequence[i] + progression
        if not isNegative[i] and isNegative[i+1]:
            expected = sequence[i] - progression
            if goingDown:
                expected = sequence[i] + progression

        if sequence[i+1] != expected:
            missing = expected

    if isAllNegative:
        missing = missing

    return missing

def find_missing2(t):
    return (t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t)