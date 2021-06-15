def encryption(code,plaintext):
    plaintext=plaintext.lower()
    cipherText=''
    for i in range(len(plaintext)):
        if plaintext[i] ==' ':
            cipherText=cipherText+plaintext[i]
        else:
            cipherText+=code[plaintext[i]]
       
    print("\nCipher Text: "+cipherText);

def decryption(code,cipherText):
    cipherText=cipherText.lower()
    plainText=''
    for i in range(len(cipherText)):
        if cipherText[i] ==' ':
            plainText=plainText+cipherText[i]
        else:
            plainText=plainText+get_key(code,cipherText[i])
        
    print("\nPlain Text: "+plainText);

def get_key(code,val): # used to get key using value from dict
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

choice = int(input("\nEnter your choice:\n1. Encrypt\n2. Decrypt\n3. Exit\n"))
if choice == 1:
    plainText=input("\nEnter plain text: ")
    encryption(code,plainText)
elif choice == 2:
    cipherText=input("\nEnter cipher text: ")
    decryption(code,cipherText)
elif choice == 3:
    exit()
else:
    print("Choose a correct Number.")