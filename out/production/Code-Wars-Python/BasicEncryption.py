def encrypt(text, rule):
    print(text, "Rule: ", rule)
    encrypted_text = ''
    for c in text:
        conversionNum = ord(c) + rule
        encrypted_text += chr(conversionNum % 256)

    return encrypted_text