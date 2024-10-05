#Given n=421649 and e=17
#n has to be factored into 2 primes p and q

def prime(n):
    for i in range(2,n//2):
        if n%i==0:
            return 0
    return 1

def check(n, e):
    for i in range(2,min(n,e)):
        if n%i==0 and e%i==0:
            return 1
    return 0

print("Enter n:")
n=int(input())
print("Enter e:")
e=int(input())

#Finding the primes p and q
for i in range(2, n//2):
    if n%i==0 and prime(i)==1 and prime(n//i)==1 and check((i-1)*((n//i)-1),e)==0 and (i-1)*((n//i)-1)>e:
        p=i
        q=n//i
        break
print("The value of p is: ", p, "and q is: ", q)

phi=(p-1)*(q-1) #Calculating the totient function
print("The value of phi is: ", phi)

#Finding the d-part of the private key (modulo phi multiplicative inverse of e)
for i in range(1,phi+1):
    if (i*e)%phi==1:
        d=i
        break
print("The value of d is: ", d) 

#Final decryption
print("Enter the input to be decrypted")
arr=list(map(int,input().split()))
ans=[]
for i in arr:
    ans.append((i**d) % n)

print("The decrypted data is")
print(*ans, sep=' ')
