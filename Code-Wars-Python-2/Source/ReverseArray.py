def reverseArray(theArray):
    for i in range(0, len(theArray) >> 1):
        lastIdx = len(theArray) - i - 1
        theArray[lastIdx], theArray[i] = theArray[i], theArray[lastIdx]
    return theArray

print(reverseArray([1,2,3,4,5,6,7,8,9,10]))

import pdb