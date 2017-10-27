from itertools import permutations
from itertools import combinations
from math import factorial
import cProfile

def removefirstindex(list):
    templist = []
    for i in range(1, len(list)):
        templist.append(list[i])
    return templist

def gta(limit, *args): # find the base_list first
    digits = []
    digitsCounter = 0
    tempDigitStr = ""
    digitsList = []
    howManyDigits = 0
    tempList = []
    multiplier7 = [1, 2, 15, 80, 300, 720, 840]
    multiplier8 = [1, 2, 18, 120, 600, 2160, 5040, 5760]
    multiplier9 = [1, 2, 21, 168, 1050, 5040, 17640, 40320, 45360]

    # convert numbers to list of individual numbers as strings
    for i in range(len(args)):
        digitsList.append(list(str(args[i])))

    # calculate how many digits in total
    for l in range(len(digitsList)):
        howManyDigits =+ howManyDigits + len(digitsList[l])


    # form digits pick first number from first list
    # move to next list, and so on... do not add duplicate numbers
    # if number is duplicated move to next list.
    # also make sure digits lenght is same as limit
    # inner as many index in digitList
    while len(digits) != limit:
        for n in range(len(digitsList)):
            # if sublist of nums is empty
            if not digitsList[n]:
                continue
            # if current digit already exists
            if digitsList[n][0] in digits:
                tempList = removefirstindex(digitsList[n])
                digitsList.pop(n)
                digitsList.insert(n, tempList)
                continue
            # else append current digit to digits list
            else:
                digits.append(digitsList[n][0])
                tempList = removefirstindex(digitsList[n])
                digitsList.pop(n)
                digitsList.insert(n, tempList)
    # Now that we are done working with string objects we
    # can convert the digits into int
    digits = list(map(int, digits))

    #print(digits)
    grandSum = 0
    #add grand total
    if len(digits) < 7:
        for i in range(1, limit + 1):
            for j in permutations(digits, i):
                grandSum =+ grandSum + sum(j)
                #print(j)
            print("Sum after one full permutation = ", grandSum)

    if len(digits) >= 7:
        for i in range(1, limit):
            if len(digits) == 7:
                grandSum = grandSum + (sum(digits)) * (len(digits) -1) * multiplier7[i]
            if len(digits) == 8:
                grandSum = grandSum + (sum(digits)) * (len(digits) -1) * multiplier8[i]
            if len(digits) == 9:
                grandSum = grandSum + (sum(digits)) * (len(digits) -1) * multiplier9[i]
            print("New iteration", grandSum)
        grandSum = grandSum + sum(digits)

    print(grandSum)

    return grandSum

cProfile.run('gta(9, 153456, 2339, 421876)')