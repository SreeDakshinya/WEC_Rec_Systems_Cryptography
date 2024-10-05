# Task:
```
Given an encrypt.c file and a password-protected .pdf file, I had to find the password that was used to protect the .pdf file. 
```

# Approach:
As the code of the encrypt.c file (custom_encrypt) took two strings as input, I realised that the hint of the previous stage ("Web.Club") could be the possible key (one of the inputs) for this custom_encrypt function. The output of this function was a stream of numbers, which was what I had obtained as the result of the previous section. This indicated that I was supposed to decrypt the given stream of numbers to find the message that was encrypted using this function. I inverted all of the operations of the custom_encrypt function to obtain the message (string) that was encrypted. 
This message worked as the password that enabled me to view the protected .pdf file. 
