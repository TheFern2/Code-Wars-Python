def encrypt_this(text):
    outputStr = ''
    text = text.split()

    for word in text:
        if len(word) == 1:
            outputStr += '{0} '.format(str(ord(word)))
        if len(word) == 2:
            outputStr += '{0}{1} '.format(str(ord(word[0])), word[1])
        if len(word) > 2:
            wordList = list(word)
            outputStr += str(ord(word[0]))
            wordList[1], wordList[-1] = wordList[-1], wordList[1]
            wordList.remove(wordList[0])
            outputStr += ''.join([str(x) for x in wordList])
            outputStr += ' '

    return outputStr[:-1]