import random
def keyGen(Text):
    key=""
    for i in range(len(Text)):
            key=key+chr(random.randint(97,122))
    print("\nkey: "+key)
    return key

def encryption(key,plaintext):
    plaintext=plaintext.lower()
    
    cipherText=''
    for i in range(len(plaintext)):
        if plaintext[i]>='a' and plaintext[i]<='z':
            base='a'
        if plaintext[i] ==' ':
            cipherText=cipherText+plaintext[i]
        else:
            encrypt= chr((ord(plaintext[i])-ord(base)+ord(key[i])-ord(base))%26 +ord(base))
            cipherText=cipherText+ (encrypt)
       
    print("\nCipher Text: "+cipherText);
    return cipherText


def decryption(key,cipherText):
    cipherText=cipherText.lower()
    plainText=''
    for i in range(len(cipherText)):
        if cipherText[i]>='a' and cipherText[i]<='z':
            base='a'
        if cipherText[i] ==' ':
            plainText=plainText+cipherText[i]
        else:
            if ord(cipherText[i])-ord(base)-ord(key[i])-ord(base)<0:
                decrypt= chr((ord(cipherText[i])-ord(key[i])+26)%26 +ord(base))
                plainText= plainText+ decrypt
            else:
                decrypt= chr((ord(cipherText[i])-ord(key[i]))%26 +ord(base))
                plainText= plainText+ decrypt

       
    print("\nPlain Text: "+plainText);




plainText=input("\nEnter plain text: ")
key=keyGen(plainText)
cipherText=encryption(key,plainText)
decryption(key,cipherText)
