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
def char_to_int(ch):
    return ord(ch) - ord('a')


def int_to_char(x):
    return chr(x + ord('a'))


def encrypt_text(text, p, e1, e2, r):
    text = text.lower().replace(" ", "")
    ct_pairs = []
    for ch in text:
        if not ch.isalpha():
            continue
        m = char_to_int(ch)  # 0-25
        ct1 = pow(e1, r, p)
        ct2 = (m * pow(e2, r, p)) % p
        ct_pairs.append((ct1, ct2))
    return ct_pairs


def decrypt_text(ct_pairs, p, d):
    plain = ""
    for ct1, ct2 in ct_pairs:
        s = pow(ct1, d, p)
        s_inv = multiplicative_invers(p, s)
        m = (ct2 * s_inv) % p
        plain += int_to_char(m)
    return plain


if __name__ == "__main__":
    # For simplicity, let user choose parameters once, then encrypt/decrypt strings
    print("--- ElGamal (string mode) ---")
    p,e1,e2,d,r = Input()
    if p == "":
        exit()

    while True:
        print("1.Encrypt string\n2.Decrypt from pairs\n3.Exit")
        c = int(input("Enter an option: "))

        if c == 1:
            text = input("Enter plaintext (letters only, e.g. hello): ")
            ct_pairs = encrypt_text(text, p, e1, e2, r)
            print("Ciphertext pairs (ct1, ct2) per character:")
            print(ct_pairs)

        elif c == 2:
            print("Enter ciphertext pairs as ct1,ct2;ct1,ct2;... e.g. 5,7;8,10")
            raw = input("Pairs: ")
            ct_pairs = []
            for part in raw.split(';'):
                part = part.strip()
                if not part:
                    continue
                a, b = part.split(',')
                ct_pairs.append((int(a), int(b)))
            pt = decrypt_text(ct_pairs, p, d)
            print("Decrypted plaintext:", pt)

        elif c == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice")


# Enter prime number p: 31
# Enter a number d: 7
# Enter a random number: 5,m=hello






