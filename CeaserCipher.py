
def encryption(key,plaintext):
    plaintext=plaintext.lower()
    
    cipherText=''
    for i in range(len(plaintext)):

        print(plaintext[i])

        if plaintext[i]>='a' and plaintext[i]<='z':
            base='a'
        if plaintext[i] ==' ':

            cipherText=cipherText+plaintext[i]
        else:
            encrypt= chr((ord(plaintext[i])-ord(base)+key)%26 +ord(base));
            cipherText=cipherText+ (encrypt)
       
    return cipherText;

def decryption(key,cipherText):
    cipherText=cipherText.lower()
    
    plainText=''
    for i in range(len(cipherText)):

        print(cipherText[i])

        if cipherText[i]>='a' and cipherText[i]<='z':
            base='a'
        if cipherText[i] ==' ':

            plainText=plainText+cipherText[i]
        else:
            encrypt= chr((ord(cipherText[i])-ord(base)-key)%26 +ord(base));
            plainText= plainText+ (encrypt)
       
    return plainText;


cipherText1=encryption(3,"Aayush Raut")
print(cipherText1)
plaintText1=decryption(3,cipherText1)
print(plaintText1)


