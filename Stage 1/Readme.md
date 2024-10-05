# Question: 
```
Let me tell you about Julius Caesar. He started using Caesar cipher, one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

The password is
YZH(878GBC 8BFC87 8C7999 F8AFB ADA8GG 8GGCC7 A7F9EG 8BFDAB)
But, is it though ?
```

# Approach:
As the question hints about Caesar Cipher, I created a new alphabet array that consisted of both alphabets and digits (as the input string consisted of both). As there are 36 such possibilities, I tried all such possibilities and noticed that one of them had all digits inside the bracket and "RSA" written outside the brackets. As RSA can be applied only to numerical inputs, this shift possibility felt like the best option. 
Hence, that was selected as the answer.
