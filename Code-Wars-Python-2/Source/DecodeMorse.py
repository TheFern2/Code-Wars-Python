def break_string(morse_code):
    words = []
    temp_word = ""
    word_started = False
    three_spaces = False
    space_count = 0
    # '.... . -.--   .--- ..- -.. .' hey jude
    # loop through string and place each word separate
    # TODO separate words by 3 spaces
    for ch in morse_code:
        #print(ord(ch))
        if not ord(ch) == 32 or word_started and ord(ch) == 32:
            temp_word += ch
            word_started = True
            space_count = 0
        if ord(ch) == 32 and three_spaces:
            words.append(temp_word)
            temp_word = ""
            three_spaces = False
            space_count = 0
        if ord(ch) == 32 and word_started:
            space_count += 1
            if space_count == 3:
                three_spaces = True

    return words

# breaks long string into words separated by 3 spaces
def break_words(morse_code):
    return morse_code.split("   ")

# check each word for extra spaces, and empty words and remove from list
def clean_word_list(word_list):
    clean_list = []
    for word in word_list:
        if word != "":
            clean_list.append(remove_whitespace(word))
    return clean_list

# only remove whitespace before and after the word
def remove_whitespace(word):
    return word.strip()

def decodeMorse(morse_code):
    #print(morse_code)
    decoded_message = []
    word_list = clean_word_list(break_words(morse_code))

    for word in word_list:
        temp_string = ""
        letters = word.split(" ")
        for letter in letters:
            converted_letter = MORSE_CODE[letter]
            temp_string += converted_letter
        decoded_message.append(temp_string)

    # ToDo: Accept dots, dashes and spaces, return human-readable message
    #return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
    return " ".join(decoded_message)

# Dictionary representing the morse code chart
morse_code_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

MORSE_CODE = {value:key for key, value in morse_code_dict.items()}

#print(decodeMorse('.... . -.--   .--- ..- -.. .'))
print(decodeMorse('   .   . '))

#print(break_words('.... . -.--   .--- ..- -.. .'))
#print(break_words('   .   . '))
#print(break_words('.... . -.--   .--- ..- -.. .'))
#print(clean_word_list(break_words('.... . -.--   .--- ..- -.. .')))