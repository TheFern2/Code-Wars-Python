def is_merge(s, part1, part2):
    print("String", s,"Part 1", part1, "Part 2",part2)
    # Will try to cheat by checking only length
    # It passes around 75% of tests
    # if len(part1) + len(part2) == len(s):
    #     return True
    # else:
    #     return False
    mergedStr = ""
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

    part1List = list(str(part2))
    part2List = list(str(part1))
    for i in range(len(s)):
        if len(part1List) != 0 and s[i] in part1List[0]:
            mergedStr = mergedStr + s[i]
            part1List.pop(0)
            continue
        if len(part2List) != 0 and s[i] in part2List[0]:
            mergedStr = mergedStr + s[i]
            part2List.pop(0)
            continue

    if mergedStr == s:
        return  True
    else:
        return False