# -*- coding: utf-8 -*-

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        #self.key = unicode(key, "utf-8")
        self.key = key.decode("utf-8")
        self.alphabet = alphabet.decode("utf-8")


    def encode(self, text):
        # key  = password
        # text = codewars
        text = text.decode("utf-8")
        transposed = self.transpose(text)
        new_position = 0
        ciphertext = ''
        cipherletter = 0
        print("Plaintext: ",text)

        # shift a-z
        for i in range(0, len(text)):
            if text[i] in self.alphabet:
                cipherletter = (self.get_position(text[i]) + self.get_position(transposed[i])) % len(self.alphabet)
                ciphertext += self.alphabet[cipherletter]
            else:
                ciphertext += text[i]
        return ciphertext.encode('utf-8')


    def decode(self, text):
        text = text.decode("utf-8")
        plaintext = ''
        plainletter = 0
        print("Ciphertext: ",text)

        transposed = self.transpose(text)

        # unshift
        for i in range(0, len(text)):
            if text[i] in self.alphabet:
                plainletter = (self.get_position(text[i]) - self.get_position(transposed[i])) % len(self.alphabet)
                plaintext += self.alphabet[plainletter]
            else:
                plaintext += text[i]
        return plaintext.encode('utf-8')

    # transpose key char by char even non alphabet chars
    def transpose(self, text):
        transposed = ""
        keyCount = 0

        for c in text:
            if keyCount % len(self.key) == 0:
                keyCount = 0
            ch = self.key[keyCount]
            transposed += ch
            keyCount += 1

        return transposed


    def get_position(self, c):
        return self.alphabet.find(c)