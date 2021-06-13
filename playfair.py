#creating 5*5 matrix with initial value 0
def create_matrix(row,column,initial_value):
    #matrix=[[initial_value]*column]*row
    matrix=[[initial_value for i in range(5)] for j in range(5)]
    return matrix

#returns the index of given element
def find_index(matrix,letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j]==letter:
                return i,j

#encrpyting plaintext
def encryption(matrix,plainText):
    cipherText=[]
    #while paring if same pair has same element adding x between them
    for i in range(0,len(plainText),2):
        if(i<len(plainText)-1):
            if plainText[i]==plainText[i+1]:
                plainText=plainText[:i+1]+'x' +plainText[i+1:]

    #adding x if odd no of element
    if len(plainText)%2!=0:
        plainText=plainText[:]+'x'

    #replacing j with i
    if 'j' in plainText:
        plainText=plainText.replace('j','i')
    print(plainText)

    #finding row and column
    for s in range(0,len(plainText),2):
        row1,column1=find_index(matrix,plainText[s])
        row2,column2=find_index(matrix,plainText[s+1])

        if row1==row2:
            cipherText.append(matrix[row1][(column1+1)%5])
            cipherText.append(matrix[row2][(column2+1)%5])
        elif column1==column2:
            cipherText.append(matrix[(row1+1)%5][column1])
            cipherText.append(matrix[(row2+1)%5][column2])
        else:
            cipherText.append(matrix[row1][column2])
            cipherText.append(matrix[row2][column1])
    
    print(''.join(cipherText))

#decrypting cipherText
def decryption(matrix,cipherText):
    plainText=[]
    #finding row and column
    for s in range(0,len(cipherText),2):
        row1,column1=find_index(matrix,cipherText[s])
        row2,column2=find_index(matrix,cipherText[s+1])
        if row1==row2:
            plainText.append(matrix[row1][(column1-1)%5])
            plainText.append(matrix[row2][(column2-1)%5])
        elif column1==column2:
            plainText.append(matrix[(row1-1)%5][column1])
            plainText.append(matrix[(row2-1)%5][column2])
        else:
            plainText.append(matrix[row1][column2])
            plainText.append(matrix[row2][column1])
    
    print(''.join(plainText))



key=input("\nEnter your key: ")
result=[]
# checking if key has repeated alphabet
for i in key:
    if i in result:
        if i=='j':
            result.append(i)
    else:
        result.append(i)

alphabets='abcdefghijklmnopqrstuvwxyz'
alphabets=list(alphabets)

# adding remaing alphabets
for i in alphabets:
    if i in result:
        pass
    else:
        if i=='j':
            pass
        else:
            result.append(i)

matrix=create_matrix(5,5,0)

#changing result to 5*5 matrix
k=0
for i  in range(0,5):
    for j in range(0,5):
        matrix[i][j]=result[k]
        k=k+1
print(matrix)


choice = int(input("\nEnter your choice:\n1. Encrypt\n2. Decrypt\n3. Exit\n"))
if choice == 1:
    plainText=input("\nEnter plain text: ")
    encryption(matrix,plainText)
elif choice == 2:
    cipherText=input("\nEnter cipher text: ")
    decryption(matrix,cipherText)
elif choice == 3:
    exit()
else:
    print("Is that a MISCLICK? Choose a correct Number.")
