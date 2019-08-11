import re

class Pair(object):
    letter = ''
    count = 0

    def __init__(self, letter, count):
        self.letter = letter
        self.count = count

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

def mix(s1, s2):

    dic1 = {}
    dic2 = {}
    sortList1 = {}
    sortList2 = {}

    s1 = cleanString(s1)
    s2 = cleanString(s2)
    dic1 = countLetters(s1)
    dic2 = countLetters(s2)
    finalStr = ''
    endString = ''
    sortList1 = sortDic(dic1, 1)
    sortList2 = sortDic(dic2, 1)
    pairs1 = []
    pairs2 = []

    # create pair objects
    for item in sortList1:
        pairs1.append(Pair(item[0], item[1]))

    for item in sortList2:
        pairs2.append(Pair(item[0], item[1]))

    # if both are empty singply return an empty string
    if not pairs1 and not pairs2:
        return ""

    # the magic begins here!
    # we want to loop until both s1 and s2 are empty
    while pairs1 or pairs2:

        i = 0

        # check if one pair is empty
        if len(pairs1) == 0 or len(pairs2) == 0:
            if len(pairs1) > 0:
                pairs1 = sorted(pairs1, key=lambda pair: pair.letter)
                for pair in pairs1:
                    finalStr += putString(1, pair.letter, pair.count)
                    #pairs1.remove(pair)

                return finalStr[:-1]

            if len(pairs2) > 0:
                pairs2 = sorted(pairs2, key=lambda pair: pair.letter)
                for pair in pairs2:
                    finalStr += putString(2, pair.letter, pair.count)
                    #pairs2.remove(pair)

                return finalStr[:-1]

        # new solution starts here
        if comparePairByCount(pairs1[i], pairs2[i]) == 0 or comparePairByCount(pairs1[i], pairs2[i]) == 3:
            tempPair = findSameCount(pairs1, pairs1[i].count)
            if hasMoreThanOne(pairs1, pairs1[i].count):
                tempPair = sorted(tempPair, key=lambda pair: pair.letter)

            tempPair2 = findSameCount(pairs2, pairs2[i].count)
            if hasMoreThanOne(pairs2, pairs2[i].count):
                tempPair2 = sorted(tempPair2, key=lambda pair: pair.letter)

            equalPairs = findEqualsInPairs(tempPair, tempPair2)
            # if len(equalPairs) > 0:
            if len(equalPairs) > 0:
                equalPairs = sorted(equalPairs, key=lambda pair: pair.letter)
                for pair in equalPairs:
                    endString += putString(0, pair.letter, pair.count)
                    pairs1.remove(pair)
                    pairs2.remove(pair)
                    tempPair.remove(pair)
                    tempPair2.remove(pair)

            # for loop each pair remaining on both tempPair
            # only find pair match, and compare if other pair is not empty
            # if other pair is empty simply add to finalString
            for pair in tempPair:
                if len(pairs2) > 0 and findOppositeLetter(pair.letter, pairs2):
                    pairMatch = findOppositeLetter(pair.letter, pairs2)
                    if comparePairByCount(pair, pairMatch) == 1:
                        finalStr += putString(1, pair.letter, pair.count)
                        pairs1.remove(pair)
                        pairs2.remove(pairMatch)
                else:
                    finalStr += putString(1, pair.letter, pair.count)
                    pairs1.remove(pair)
                    #pairs2.remove(pairMatch)

            for pair in tempPair2:
                if len(pairs1) > 0 and findOppositeLetter(pair.letter, pairs1):
                    pairMatch = findOppositeLetter(pair.letter, pairs1)
                    if comparePairByCount(pairMatch, pair) == 2:
                        finalStr += putString(2, pair.letter, pair.count)
                        pairs1.remove(pairMatch)
                        pairs2.remove(pair)
                else:
                    finalStr += putString(2, pair.letter, pair.count)
                    pairs2.remove(pair)

            finalStr += endString
            endString = ''
            #clear lists here!
            del equalPairs[:]
            del tempPair[:]
            del tempPair2[:]

            continue

        # if m6 > n5
        if comparePairByCount(pairs1[i], pairs2[i]) == 1:

            tempPair = findSameCount(pairs1, pairs1[i].count)
            if hasMoreThanOne(pairs1, pairs1[i].count):
                tempPair = sorted(tempPair, key=lambda pair: pair.letter)

            for pair in tempPair:
                if len(pairs2) > 0 and findOppositeLetter(pair.letter, pairs2):
                    pairMatch = findOppositeLetter(pair.letter, pairs2)
                    if comparePairByCount(pair, pairMatch) == 1:
                        finalStr += putString(1, pair.letter, pair.count)
                        pairs1.remove(pair)
                        pairs2.remove(pairMatch)
                else:
                    finalStr += putString(1, pair.letter, pair.count)
                    pairs1.remove(pair)

            continue

        # if m3 < m6
        if comparePairByCount(pairs1[i], pairs2[i]) == 2:

            tempPair2 = findSameCount(pairs2, pairs2[i].count)
            if hasMoreThanOne(pairs2, pairs2[i].count):
                tempPair2 = sorted(tempPair2, key=lambda pair: pair.letter)

            for pair in tempPair2:
                if len(pairs1) > 0 and findOppositeLetter(pair.letter, pairs1):
                    pairMatch = findOppositeLetter(pair.letter, pairs1)
                    if comparePairByCount(pairMatch, pair) == 2:
                        finalStr += putString(2, pair.letter, pair.count)
                        pairs1.remove(pairMatch)
                        pairs2.remove(pair)
                else:
                    finalStr += putString(2, pair.letter, pair.count)
                    pairs2.remove(pair)

    return finalStr[:-1]


def findEqualsInPairs(pair1, pair2):
    equalPairs = []
    for pairItem in pair1:
        for pairItem2 in pair2:
            if pairItem == pairItem2:
                equalPairs.append(pairItem)

    return equalPairs



def findOppositeLetter(letter, pairs):
    for item in pairs:
        if item.letter == letter:
            return item

def findSameCount(pairList, letterCount):
    tempList = []
    for item in pairList:
        if item.count == letterCount:
            tempList.append(item)
    return tempList

# checks if dic has more than one tuple with same count
def hasMoreThanOne(pairList, count):
    counter = 0
    for item in pairList:
        if item.count == count:
            counter += 1
    if counter > 1:
        return True
    else:
        return False

def cleanString(str):
    # get rid of non a-z
    regex = re.compile('[^a-z]')
    #First parameter is the replacement, second parameter is your input string
    str = regex.sub('', str)
    regex.sub()
    return str

def countLetters(str):
    letterDic = {}

    for c in str:
        if str.count(c) == 1:
            continue
        letterDic[c] = str.count(c)

    return letterDic


# 0 for letter, 1 for count
# reverse=True by default, set to false when doing letters
def sortDic(dic, mode, isReverse=True):
    #how does lambda work?
    dic = sorted(dic.items(), key=lambda x:x[mode], reverse=isReverse)
    return dic


# 0 for letter, 1 for count
def comparePairByCount(pair1, pair2):

    # 0 is equal, 1 when s1 is greater, 2 when s2 is greater
    # n5 == n5
    if pair1 == pair2:
        return 0
    # m6 > n5
    if pair1.count > pair2.count:
        return 1
    # m5 < n6
    if pair1.count < pair2.count:
        return 2
    # m5 == n5
    if pair1.count == pair2.count:
        return 3


def putString(lead, letter, count, isLast=False):
    # '{0}{1}'.format('abc', 'def')
    formedString = ''

    if isLast:
        if lead == 0:
            formedString = '=:{0}'.format(letter*count)
        if lead == 1:
            formedString = '{0}:{1}'.format(lead, letter*count)
        if lead == 2:
            formedString = '{0}:{1}'.format(lead, letter*count)
    else:
        if lead == 0:
            formedString = '=:{0}/'.format(letter*count)
        if lead == 1:
            formedString = '{0}:{1}/'.format(lead, letter*count)
        if lead == 2:
            formedString = '{0}:{1}/'.format(lead, letter*count)
    
    return formedString


# By https://www.codewars.com/users/Unnamed
from collections import Counter

def mix2(s1, s2):
    c1 = Counter(filter(str.islower, s1))
    c2 = Counter(filter(str.islower, s2))
    res = []
    for c in set(c1 + c2):
        n1, n2 = c1.get(c, 0), c2.get(c, 0)
        if n1 > 1 or n2 > 1:
            res.append(('1', c, n1) if n1 > n2 else
                       ('2', c, n2) if n2 > n1 else ('=', c, n1))
    res = ['{}:{}'.format(i, c * n) for i, c, n in res]
    return '/'.join(sorted(res, key=lambda s: (-len(s), s)))


# By https://www.codewars.com/users/nkrause323
def mix3(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))
