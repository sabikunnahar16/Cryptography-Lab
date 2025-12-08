import math

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a


def isprime(n):
    if n<=1:
        return False
    for i in range(2,math.ceil(math.sqrt(n))):
        if n%i ==0:
            return False
    return True

def prime_factors(n):
    pf = set()
    d = 2

    while d*d <= n:
        while n%d == 0:
            pf.add(d)
            n//=d
        
        d+=1 if d == 2 else 2
    
    if n>1:
        pf.add(n)
    
    return pf

def primitive_root(p):
    if p == 2:
        return 1
    
    phi = p-1
    factors = prime_factors(phi)

    for i in range(2,p):
        ok = True
        for q in factors:
            if pow(i,phi//q,p)==1:
                ok = False
                break
        if ok:
            return i
    
    return None


def Input():
    p = int(input("Enter prime number p: "))

    if not isprime(p):
        print("Please use two prime number")
        return "","","","",""

    d = int(input("Enter a number d: "))

    r = int(input("Enter a random number: "))

    # d must be in [1, p-2] and coprime with (p-1)
    if d < 1 or d > p-2 or gcd(p-1, d) != 1:
        print("Please use correct d value")
        return "","","","",""
    
    e1 = primitive_root(p)
    e2 = (e1**d) % p

    return p,e1,e2,d,r

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


while True:
    print("1.Key_generation\n2.Encryption\n3.Decryption\n4.Exit")
    c = int(input("Enter an option: "))

    if c == 1:
        p,e1,e2,d,r = Input()
        if p=="" and e1 == "" and d=="" and e2=="" and r=="":
            continue

    elif c == 2:
        pt = int(input("Enter plain-message: "))
        ct1 = (e1**r)%p
        ct2 = (pt*(e2**r))%p
        print("Cipher message1: ",ct1)
        print("Cipher message2: ",ct2)
        
    elif c==3:
        ct1 = int(input("Enter cipher-message1: "))
        ct2 = int(input("Enter cipher-message2: "))
        # s = (ct1^d mod p), then find its inverse modulo p
        s = pow(ct1, d, p)
        s_inv = multiplicative_invers(p, s)
        pt = (ct2 * s_inv) % p
        print("Plain message: ",pt)
        
    elif c==4:
        print("Exiting...")
        break
        
    else:
        continue



# Enter an option: 1,public(e1,e2,p),private=d=3,random r=4
# Enter prime number p: 11
# Enter a number d: 3
# Enter a random number: 4 
        
    







