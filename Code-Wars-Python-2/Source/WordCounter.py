# My first python program ever passed all tests :)
# coding: utf-8

import unittest

def remove_non_ascii_2(s):
    return ''.join([i if ord(i) < 128 else ' ' for i in s])

def isSpecialChar(c):
    if ord(c) >= 33 and ord(c) <= 47 or ord(c) >= 58 and ord(c) <= 64:
        return True
    elif ord(c) >= 91 and ord(c) <= 96 or ord(c) >= 123 and ord(c) <= 126:
        return True
    #elif ord(c) == 226: #testing for right single quotation might need a list here is counting as 3 chars
    #    return True
    else:
        return False

def word_count(s):
    wordCount = 0
    tempString = ''
    listOfWords = []
    unwantedWords = (["a","the","on","at","of","upon","in", "as"])
    charFound = False
    charIndex = 0;
    lastIndex = 0;
    isLastIndex = False
    isUnicode = False
    unicodeAddedToIndex = False
    sameWordsCount = 0
    
    # find the last index of the string
    lastIndex = (len(s) -1)
    #print('Last index is',lastIndex)
    
    # wordCount words, which s contains
    # do not wordCount the following a, the, on, at, of, upon, in, as - case insensitive
    
    # if is a lower or upper case, append char to a string
    for char in s:
        #print(ord(char))
        # check index
        if charIndex == lastIndex:
            isLastIndex = True
        if ord(char) == 226 and not unicodeAddedToIndex:
            #charIndex += 1
            unicodeAddedToIndex = True
            isUnicode = True
        if char.islower() or char.isupper():
            tempString += char
            charFound = True
            #charIndex += 1
        if (isSpecialChar(char) or char.isdigit() or char.isspace() or isLastIndex or isUnicode) and charFound:
            listOfWords.append(tempString)  # add string to a list
            wordCount += 1
            print(tempString, wordCount)
            charFound = False
            tempString = ''
        #else:
        #    print('Special character')
        charIndex += 1
        if ord(char) == 226:
            charIndex - 2 # Because a unicode goes 3 times thru the for loop we substract 2
        unicodeAddedToIndex = False
        isUnicode = False
        
    #return wordCount
    
    # check with words equal to the doNotCountList, and substract wordCount
    # make sure strings are not case sensitive this one drove me crazy!
    for str1 in listOfWords:
        for str2 in unwantedWords:
            if str1.lower() == str2.lower():
                wordCount -= 1
                sameWordsCount += 1
                print(str1, str2, sameWordsCount)
    
    # finally wordCount the words
    return wordCount
    
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEquals(word_count("hello there"), 2)
        self.assertEquals(word_count("hello there and a hi"), 4)
        self.assertEquals(word_count("I'd like to say goodbye"), 6)
        self.assertEquals(word_count("Slow-moving user6463 has been here"), 6)
        self.assertEquals(word_count("%^&abc!@# wer45tre"), 3)
        self.assertEquals(word_count("abc123abc123abc"), 3)
        self.assertEquals(word_count("Really2374239847 long ^&#$&(*@# sequence"), 3)
        self.assertEquals(word_count("I’d been using my sphere as a stool. I traced counterclockwise circles on it with my fingertips and it shrank until I could palm it. My bolt had shifted while I’d been sitting. I pulled it up and yanked the pleats straight as I careered around tables, chairs, globes, and slow-moving fraas. I passed under a stone arch into the Scriptorium. The place smelled richly of ink. Maybe it was because an ancient fraa and his two fids were copying out books there. But I wondered how long it would take to stop smelling that way if no one ever used it at all; a lot of ink had been spent there, and the wet smell of it must be deep into everything."), 112)
        
    def test2(self):
        # This is the only test failed on first submission
        # 1-18, 2-38, 3-60, 4-81, 5-101, 6-125, 7-145, 8-166, 9-192, 10-202
        longText = """The Mynster had a ceiling of stone, steeply vaulted. Above the vaults, a flat roof had been framed. 
        Built upon that roof was the aerie of the Warden Fendant. Its inner court, squared around the Præsidium, was roofed 
        and walled and diced up into store-rooms and headquarters, but its periphery was an open walkway on which the Fendant’s 
        sentinels could pace a full circuit of the Mynster in a few minutes’ time, seeing to the horizon in all directions 
        (except where blocked by a buttress, pier, spire, or pinnacle). This ledge was supported by dozens of close-spaced braces 
        that curved up and out from the walls below. The end of each brace served as a perch for a gargoyle keeping eternal vigil. 
        Half of them (the Fendant gargoyles) gazed outward, the other half (the Regulant gargoyles) bent their scaly necks and aimed 
        their pointy ears and slitted eyes into the concent spread below. Tucked between the braces, and shaded below the sentinels’ walkway, 
        were the squat Mathic arches of the Warden Regulant’s windows. Few places in the concent could not be spied on from at least one of 
        these— and, of course, we knew them all by heart."""
        
        self.assertEquals(word_count(longText), 160)
        
    def test3(self):
        longtext = """Hun så bort og smilte flere ganger til kjæresten, OL-roeren Nils Jakob Hoff.
                    Han satt på første rad med notatblokk i den lille losjen med utsikt over den tildekkede gressmatten på landslagsarenaen. Smilte tilbake.
                    I fire minutter hadde blitzregnet fra kameraene til fotografene dundret mot henne, bare 40–50 centimeter unna.
                    En tydelig preget Johaug festet ikke øynene i noen av dem. Så litt ned, lot blikket gå litt fem og tilbake.
                    Da hun selv skulle sette seg i vitneboksen, kjempet Johaig for å holde tårene tilbake."""
                    
        self.assertEquals(word_count(longtext), 86)
        