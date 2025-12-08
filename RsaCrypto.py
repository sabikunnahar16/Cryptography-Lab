import math


def isprime(n):
    if n<=1:
        return False
    for i in range(2,math.ceil(math.sqrt(n))):
        if n%i ==0:
            return False
    return True

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def multiplicative_invers(a,b):
    r1 = a
    r2 = b
    t1 = 0
    t2 = 1

    while r2!=0:
        q = r1 // r2
        r = r1%r2
        t = t1-q*t2

        r1 = r2
        r2 = r
        t1 = t2
        t2 = t 
    return t1%a


def Input():
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))

    if not isprime(p) or not isprime(q):
        print("Please use two prime number")
        return "","",""
    if p == q:
        print("Please use two separate prime number")
        return "","",""
    
    n = p*q
    phi_n = (p-1)*(q-1)

    e = int(input("Enter a number e: "))

    if e<=1 or e>=phi_n or gcd(phi_n,e)!=1:
        print("Please use correct e value")
        return "","",""
    
    d = multiplicative_invers(phi_n,e)

    return e,d,n






while True:
    print("1.Key_generation\n2.Encryption\n3.Decryption\n4.Exit")
    c = int(input("Enter an option: "))

    if c == 1:
        e,d,n = Input()
        if e == "" and d=="" and n=="":
            continue

    elif c == 2:
        pt = int(input("Enter plain-message: "))
        ct = (pt**e)%n
        print("Cipher message: ",ct)
        
    elif c==3:
        ct = int(input("Enter cipher-message: "))
        pt = (ct**d)%n
        print("Plain message: ",pt)
        
    elif c==4:
        print("Exiting...")
        break
        
    else:
        continue



#   p=7,q=11,e=13,m=5,public key=(e,n)=(13,77)
#   c= (m^e)mod n = (5^13)mod 77,M=c^d mod n
#     d=37,private key=(d,)  
        
    







