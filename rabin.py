import math


def isprime(n):
    if n<=1:
        return False
    for i in range(2,math.ceil(math.sqrt(n))):
        if n%i ==0:
            return False
    return True

def multiplicative_invers(a,b):
    if b > a:
        b = b%a
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

    if  p%4!=3 or q%4!=3 or p==q :
        print("Please use two valid prime number")
        return "","",""
    
    
    n = p*q

    return p,q,n



while True:
    print("1.Key_generation\n2.Encryption\n3.Decryption\n4.Exit")
    c = int(input("Enter an option: "))

    if c == 1:
        p,q,n = Input()
        if p == "" and q=="" and n=="":
            continue

    elif c == 2:
        pt = int(input("Enter plain-message: "))
        ct = (pt**2)%n
        print("Cipher message: ",ct)
        
    elif c==3:
        ct = int(input("Enter cipher-message: "))

        a1 = (ct**((p+1)//4))%p
        a2 = (-ct**((p+1)//4))%p
        b1 = (ct**((q+1)//4))%q
        b2 = (-ct**((q+1)//4))%q

        pairs = [[a1,b1],[a1,b2],[a2,b1],[a2,b2]]

        n1 = n//p
        n2 = n//q
        
        y1 = multiplicative_invers(p,n1) 
        y2 = multiplicative_invers(q,n2) 

        k=0
        pts = []
        for pair in pairs:
            m = ((pair[0]*n1*y1)+(pair[1]*n2*y2))%n
            pts.append(m)
            print(f"M{k+1}: {m}")
            k+=1
        
        flag = True
        for i in range(len(pts)-1):
            a = (pts[i]**2)%n
            b = (pts[i+1]**2)%n
            if a!=b:
                flag = False
                break
        
        if flag:
            print("Valid Decryption")
        
        else:
            print("Invalid Decryption")
        
    elif c==4:
        print("Exiting...")
        break
        
    else:
        continue

# p=23,q=7,m=24

    
        
    







