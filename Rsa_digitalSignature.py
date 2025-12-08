import math

# --------------------- BASIC FUNCTIONS ---------------------

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# --------- LINEAR SEARCH MULTIPLICATIVE INVERSE (NEW) ---------

def multiplicative_invers(e, phi):
    """
    Find d such that (e * d) % phi = 1
    using linear search instead of Euclid.
    """
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None   # if no inverse exists


# --------------------- KEY INPUT ---------------------

def Input():
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))

    if not isprime(p) or not isprime(q):
        print("Please use two prime numbers")
        return "", "", ""

    if p == q:
        print("Please use two different primes")
        return "", "", ""

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = int(input("Enter a number e: "))

    if e <= 1 or e >= phi_n or gcd(phi_n, e) != 1:
        print("Please use correct e value")
        return "", "", ""

    d = multiplicative_invers(e, phi_n)

    if d is None:
        print("Multiplicative inverse not found")
        return "", "", ""

    return e, d, n


# --------------------- MAIN PROGRAM ---------------------

while True:
    print("1. Key_generation\n2. Encryption\n3. Decryption\n4. Exit")
    c = int(input("Enter an option: "))

    if c == 1:
        e, d, n = Input()
        if e == "" and d == "" and n == "":
            continue
        print("Public Key (e, n): ", e, n)
        print("Private Key (d, n): ", d, n)

    elif c == 2:
        pt = int(input("Enter plain-message (integer): "))
        ct = (pt ** e) % n
        print("Cipher message: ", ct)

    elif c == 3:
        ct = int(input("Enter cipher-message: "))
        pt = (ct ** d) % n
        print("Plain message: ", pt)

    elif c == 4:
        print("Exiting...")
        break

    else:
        print("Invalid option")
        continue
# Enter prime number p: 7
# Enter prime number q: 11
# Enter a number e: 7,m=15