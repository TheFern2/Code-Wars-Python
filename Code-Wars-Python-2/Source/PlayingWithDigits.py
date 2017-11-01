def dig_pow(n, p):
    # convert numbers to list of individual numbers as strings
    numStr = str(n)
    result = 0
    power = p
    for i in range(len(numStr)):
        result = result + (pow(int((numStr[i])),power))
        power = power + 1
    # check result
    if result % n == 0:
        return result / n
    else:
        return -1