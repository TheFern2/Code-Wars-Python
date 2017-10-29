from itertools import permutations
from itertools import combinations
from math import factorial
import cProfile

def remove_first_index(list):
    templist = []
    for i in range(1, len(list)):
        templist.append(list[i])
    return templist

def permutation_count(n, r):
    return int(factorial(n) / factorial((n - r)))

def gta(limit, *args): # find the base_list first
    digits = []
    digitsCounter = 0
    tempDigitStr = ""
    digitsList = []
    howManyDigits = 0
    tempList = []

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
    # [1, 5, 6, 2, 7, 3, 4, 8, 9]
    j = 0
    while len(digits) != limit:
        #for n in range(len(digitsList)):
        # if sublist of nums is empty
        if not digitsList[j]:
            if j < len(args) -1:
                j = j + 1
                continue
            if j == len(args) -1:
                j = 0
        # if current digit already exists
        if digitsList[j][0] in digits:
            tempList = remove_first_index(digitsList[j])
            digitsList.pop(j)
            digitsList.insert(j, tempList)
            if j < len(args) -1:
                j = j + 1
            if j == len(args) -1:
                j = 0
        # else append current digit to digits list
        else:
            digits.append(digitsList[j][0])
            tempList = remove_first_index(digitsList[j])
            digitsList.pop(j)
            digitsList.insert(j, tempList)
            if j < len(args) -1:
                j = j + 1
                continue
            if j == len(args) -1:
                j = 0
    # Now that we are done working with string objects we
    # can convert the digits into int
    digits = list(map(int, digits))

    grandSum = 0
    #add grand total
    #if len(digits) < 7:
    # for i in range(1, limit + 1):
    #     for j in permutations(digits, i):
    #         grandSum =+ grandSum + sum(j)
    #         print(j)
    #     print("Sum after one full permutation = ", grandSum)

    for i in range(2, limit + 1):
        grandSum = grandSum + (sum(digits) * (permutation_count(len(digits), i) / len(digits) * i))

    grandSum = grandSum + sum(digits)
    print(grandSum)

    return grandSum