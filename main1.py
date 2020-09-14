from random import randint

#open file
f = open("C:\\Users\\toshi\\OneDrive\\Desktop\\CaesarCipher\\Caesar.txt","r")


originalText = ""
encryptedText = ""

#copy text into a string
for line in f:
    originalText += line

#create shift amount
shift = randint(1,25)
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#start encrypting letters only
for character in originalText:
    #handles lower case
    if 97<=ord(character)<=122:
        encryptedChar = lowerCase.index(character) + shift
        if encryptedChar > 25:
          encryptedChar = (encryptedChar % 25) - 1
        encryptedText += lowerCase[encryptedChar]
    #handles upper case
    elif 65 <= ord(character) <= 90:
        encryptedChar = upperCase.index(character) + shift
        if encryptedChar > 25:
            encryptedChar = (encryptedChar % 25) - 1
        encryptedText += upperCase[encryptedChar]
    #handles everything else
    else:
        encryptedText += character
#close the original file
f.close()
#print to new file
y = open(r"C:\Users\toshi\OneDrive\Desktop\CaesarCipher\encrypted.txt", "w")
y.write(encryptedText)
y.close()


