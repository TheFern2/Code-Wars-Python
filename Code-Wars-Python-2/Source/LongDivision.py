
# Multiply divisor by n quotient and return the result
def multiply(divisor, quotient):
    divisorList = list(map(int, divisor))
    result = carry = 0
    resultStr = ""
    dividend = []
    properResultStr = ""
    for num in divisorList[::-1] + [-1]:
        if num == -1 and carry >= 1:
            dividend.append(carry)
            break
        result = (quotient * num) + carry
        resultStr = str(result)
        if result >= 10:
            carry = result // 10
            result = int(resultStr[-1])
        elif result < 10:
            carry = 0
            result = int(resultStr[0])
        dividend.append(result)
    #properResultStr = "".join(str(x) for x in currentDividend)
    #print(properResultStr[::-1])
    return dividend[::-1]

# receives lists of divisor and dividend for easier processing
# top is initial dividend (at minus new dividend result)
# bottom is new dividend
def substraction(top, bottom):
    top = top[0:len(bottom)]
    top = top[::-1]
    bottom = bottom[::-1]
    result = carry = 0
    subResult = []
    #print("top", top)
    #print("bottom", bottom)

    for i in range(len(top)):
        if top[i] >= bottom[i]:
            result = top[i] - (bottom[i] + carry)
            subResult.append(result)
            carry = 0
        elif top[i] < bottom[i]:
            result = (top[i] + 10) - (bottom[i] + carry)
            subResult.append(result)
            carry = 1

    # need to make sure last one is not a zero, if is remove
    # might need to do a for loop here in case of more zero's
    if subResult[-1] == 0:
        subResult.pop(-1)
    # and reverse to return correct result
    #print(subResult[::-1])
    return subResult[::-1]

def divide(dividend,divisor):
    divisorList = list(map(int, divisor))
    dividendList = list(map(int, dividend))
    currentDividend = []
    quotient = []
    subtractionResult = []
    quotientStr = ""
    remainderStr = ""

    # Find start and initial quotient
    if divisorList[0] > dividendList[0]:
        start = len(divisor) + 1
        quotient.append(int(dividend[0:2]) // divisorList[0])
        # else start at divisor length
    else:
        start = len(divisor)
        quotient.append(dividendList[0] // divisorList[0])
    #print(start, quotient)

    currentDividend = multiply(divisor, quotient[0])
    subtractionResult = substraction(dividendList, currentDividend)

    # Loop through the rest
    for i in range(len(dividend) - (start)):
        # check if MLN(Divisor) is > MLN(Dividend)
        # if it is start at divisor length + 1
        if divisorList[0] > subtractionResult[0]:
            currentNum = ''.join(str(subtractionResult[i]) for i in range(0, 2))
            quotient.append( int(currentNum) // divisorList[0])
        # else start at divisor length
        else:
            quotient.append(subtractionResult[0] // divisorList[0])
        #print(quotient)

        currentDividend = multiply(divisor, quotient[i + 1])
        subtractionResult.append(dividendList[start + i])
        subtractionResult = substraction(subtractionResult, currentDividend)

    quotientStr = ''.join(str(q) for q in quotient)
    remainderStr = ''.join(str(r) for r in subtractionResult)
    #remainderStr = [s.lstrip("0") for s in remainderStr]

    print("Quotient = ", quotientStr)
    print("Remainder = ", remainderStr)

    return quotientStr, remainderStr

#divide("1786076652", "4031214")
#divide("708786169050364264498483629949124333050732544381974635927181624935149734520700893406021846629015886556979336613266067831305308408103158793977395210", "7940654497315444076393326654563424600027591749183996881831501175073708180868620549933284")
divide("981866229000", "125300")
#print(multiply("4031214", 4))
#substraction(17860766)