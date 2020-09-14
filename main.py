#open encrypted file
f = open(r"C:\Users\toshi\OneDrive\Desktop\CaesarCipher\encrypted.txt", "r")

encryptedText = ""
originalText = ""
for line in f:
    encryptedText += line

#upper and lower case
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
y = open(r"C:\Users\toshi\OneDrive\Desktop\CaesarCipher\allOutputs.txt", "w")
for i in range(1,26):
    for character in encryptedText:
        if 97 <= ord(character) <=120:
            new_index = lowerCase.index(character) - i
            if new_index < 0:
                new_index = new_index + 26
            originalText += lowerCase[new_index]
        elif 65 <= ord(character) <= 90:
            new_index = upperCase.index(character) - i
            if new_index < 0:
                new_index = new_index + 26
            originalText += upperCase[new_index]
        else:
            originalText += character
    y.write("This is the decryption for shift of %s" % i)
    y.write(".\n")
    y.write(originalText)
    y.write("\n\n")
    originalText = ""

y.close()