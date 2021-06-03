def encryption(code,plaintext):
    plaintext=plaintext.lower()
    
    cipherText=''
    for i in range(len(plaintext)):

        print(plaintext[i])
        if plaintext[i] ==' ':

            cipherText=cipherText+plaintext[i]
        else:
            cipherText+=code[plaintext[i]]
       
    return cipherText

def decryption(code,cipherText):

    cipherText=cipherText.lower()
    
    plainText=''
    for i in range(len(cipherText)):
        if cipherText[i] ==' ':
            plainText=plainText+cipherText[i]
        else:
            plainText=plainText+get_key(cipherText[i])
        
    return plainText;

def get_key(val): # used to get key using value from dict
    for key, value in code.items():
         if val == value:
             return key

normalChar = "abcdefghijklmnopqrstuvwxyz"
codedChar = "qwertyuiopasdfghjklzxcvbnm"
normalChar = list(normalChar)
codedChar=list(codedChar)

code={} # dict of normalChar and codedChar
for i in range(26):
    code[normalChar[i]]=codedChar[i]

plaintext='Hello World'
cipherText1=encryption(code,plaintext)
print(cipherText1)
plainText1=decryption(code,cipherText1)
print(plainText1)