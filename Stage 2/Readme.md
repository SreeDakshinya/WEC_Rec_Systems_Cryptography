# Question: 
```
This is stage 2.
Info on encrypter's public key:
n = 421649
e = 17

Remember if you are stuck somewhere "Web.Club" will help you.
```

# Approach:
The given inputs are a pair of public key values for the RSA encryption scheme (RSA was hinted at in the previous stage). In order to decrypt such a message, one would need a private key, which consists of n and d. 
First, two prime factors ```(p, q)``` of ```n``` have to be identified, such that ```(p-1)\*(q-1)``` is greater than and is co-prime with ```e```. This ```(p-1)*(q-1)``` is called as ```phi(n)``` and is called as totient function of n. d is then calculated as the multiplicative inverse of e wrt modulo phi(n).
The final decryption is performed as: ```(data)^d mod n```, where data is the encrypted data which is to be decrypted. 
The output of this is used as the password to unlock the .zip file of the final stage. 
