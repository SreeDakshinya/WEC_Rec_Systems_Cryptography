#Given the encrypt.c file, using the output of the previous stage as the encrypted data and key as "Web.Club", finding the message by inverting the procedures of the encrypt.c file

msg=[]

print("Enter the encrypted data")
enc=list(map(int,input().split()))

print("Enter the key")
key_text=input()
key=[]
#Converting the text to ASCII format
for i in range(len(key_text)):
    key.append(ord(key_text[i]))

#Inverting the operations performed in the custom_encrypt function of the .c file
for i in range(len(enc)):
    r=enc[i]
    while 1:
        if i==0:
            if (r)/key[i]==(r)//key[i]:
                msg.append((r)//key[i])
                break
        else:
            if (r-enc[i-1])/key[i]==(r-enc[i-1])//key[i]:
                msg.append((r-enc[i-1])//key[i])
                break
        r=r+10000

#Converting the ASCII output to text format (as the message was a textual input in the .c file)
out=[]
for i in range(len(msg)):
    out.append(chr(msg[i]))
print(*out, sep='')
    
