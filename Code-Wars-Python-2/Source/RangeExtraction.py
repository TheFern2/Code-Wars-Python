

def checkNextThree(args, i):
    if i < len(args)-2 and args[i] + 1 == args[i+1] and args[i+1] + 1 == args[i+2]:
        return True
    else:
        return False

def solution(args):
    # [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
    # [-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')
    print(args)
    tempRange = []
    extraction = ""
    counter = 0
    flag = False
    finishedRange = False

    for i in range(len(args)-1):
        finishedRange = False
        # if next number is sequential add to list
        nextNumber = args[i] + 1
        if args[i+1] == nextNumber:
            if len(tempRange) == 0:
                tempRange.append(args[i])
            tempRange.append(args[i+1])
            flag = True
            counter += 1
        # else add to string
        else:
            # add first and last from range list
            if flag and counter >= 2:
                if i == len(args)-1:
                    extraction += "%s-%s," % (tempRange[0],tempRange[-1])
                else:
                    if not checkNextThree(args, i+1):
                        extraction += "%s-%s" % (tempRange[0],tempRange[-1])
                    else:
                        extraction += "%s-%s" % (tempRange[0],tempRange[-1])
                del tempRange[:]
                flag = False
                counter = 0
                finishedRange = True
                #continue
            if flag and counter == 1:
                if i == 1:
                    extraction += "%s,%s" % (tempRange[0],tempRange[-1])
                else:
                    extraction += ",%s" % str(args[i])
                del tempRange[:]
                flag = False
                counter = 0
                finishedRange = True
                #continue
            # add current number
            #extraction += str(args[i+1])
            if len(extraction) == 0:
                extraction += "%s" % str(args[i])
                #continue
            if checkNextThree(args, i+1):
                extraction += ","
                continue
            if not checkNextThree(args, i+1):
                extraction += ",%s" % str(args[i+1])




    if counter >= 2 and len(tempRange) != 0:
        extraction += "%s-%s" % (tempRange[0],tempRange[-1])
    if counter == 1 and len(tempRange) != 0:
        extraction += ",%s" % tempRange[-1]


    print(extraction)

    return extraction