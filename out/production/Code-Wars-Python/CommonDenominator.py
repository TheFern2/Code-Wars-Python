from functools import reduce

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""
    return reduce(lcm, args)


def convertFracts(lst):
    print(lst)
    denominatorList = []
    lowestCommonMultiple = 0
    convertedFractions = []
    tempMultiplier = 0
    # get denominator list
    for i in range(len(lst)):
        denominatorList.append(lst[i][1])

    # find lcm
    lowestCommonMultiple = lcmm(*denominatorList)

    # form list with fractions
    for i in range(len(lst)):
        tempMultiplier = int(lowestCommonMultiple / lst[i][1])
        convertedFractions.append([lst[i][0] * tempMultiplier, lowestCommonMultiple])

    return convertedFractions