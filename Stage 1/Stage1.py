arr=list(input()) #taking input
#stream of characters
table=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ans=[]
for k in range(36): #checking for all 36 (for this alphabet) Caesar-Cipher shift possibilities
    for i in range(len(arr)):
        if arr[i]==' ' or arr[i] in ['(', ')']:
            ans.append(arr[i])
        else:
            ans.append(table[(table.index(arr[i])+k)%36])
    print(k, '-', *ans, sep='')
    print()
    ans=[]
