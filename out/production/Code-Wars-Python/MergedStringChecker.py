def mergeFrontLetters(s, part1, part2):
    part1List = list(str(part2))
    part2List = list(str(part1))
    mergedStr = ""

    for i in range(len(s)):
        if len(part1List) != 0 and s[i] in part1List[0]:
            mergedStr = mergedStr + s[i]
            part1List.pop(0)
            continue
        if len(part2List) != 0 and s[i] in part2List[0]:
            mergedStr = mergedStr + s[i]
            part2List.pop(0)
            continue
    return mergedStr

def mergeReversed(s, part1, part2):
    part1 = part1[::-1]
    part2 = part2[::-1]
    s = s[::-1]
    part1List = list(str(part1))
    part2List = list(str(part2))
    mergedStr = ""
    for i in range(len(s)):
        if len(part1List) != 0 and s[i] in part1List[0]:
            mergedStr = mergedStr + s[i]
            part1List.pop(0)
            continue
        if len(part2List) != 0 and s[i] in part2List[0]:
            mergedStr = mergedStr + s[i]
            part2List.pop(0)
            continue
    return mergedStr

def is_merge(s, part1, part2):
    print("String", s,"Part 1", part1, "Part 2",part2)
    # Will try to cheat by checking only length
    # It passes around 75% of tests
    # if len(part1) + len(part2) == len(s):
    #     return True
    # else:
    #     return False
    mergedStr = ""
    mergedStr2 = ""
    reverseStr = ""
    reverseInputStr = s[::-1]
    # digitsList.append(list(str(args[i])))

    #First check the obvious
    mergedStr = part1+part2
    if mergedStr == s:
        return True
    if not s:
        return False
    if len(part1) + len(part2) > len(s):
        return False
    else:
        mergedStr = ""

    mergedStr = mergeFrontLetters(s, part1, part2)
    mergedStr = mergeFrontLetters(s, part2, part1)
    reverseStr = mergeReversed(s, part1, part2)

    print(reverseStr)

    if mergedStr == s:
        return  True
    elif mergedStr2 == s:
        return True
    elif reverseStr == reverseInputStr:
        return True
    else:
        return False