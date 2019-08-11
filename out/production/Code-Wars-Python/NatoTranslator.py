#!/usr/bin/python
import unittest
from WordCounter import isSpecialChar

# method checks for special chars according with ascii
def isSpecialChar(c):
    if ord(c) >= 33 and ord(c) <= 47 or ord(c) >= 58 and ord(c) <= 64:
        return True
    elif ord(c) >= 91 and ord(c) <= 96 or ord(c) >= 123 and ord(c) <= 126:
        return True
    else:
        return False

def to_nato(words):
    words = words.replace(" ", "") # remove spaces here
    print(words) # console output
    listOfPhonetics = []
    
    # create dictionary with Nato phonetics
    natoDic = {'A':'Alfa', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'H': 'Hotel', 'I':'India', 'J':'Juliett', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}
    
    for letter in words:
        if(isSpecialChar(letter)):              #IF... special character add to the list
            listOfPhonetics.append(letter)   
        else:                                   #ELSE... retrieve from dictionary, and append to the list
            listOfPhonetics.append(natoDic.get(letter.upper()))
    
    myListStr = ' '.join(map(str, listOfPhonetics)) #JOIN... list as a string with spaces
    
    return myListStr    
    
    
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEquals(to_nato('If you can read'), "India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta")
        self.assertEquals(to_nato('Did not see that coming'), "Delta India Delta November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf")