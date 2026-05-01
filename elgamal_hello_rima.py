from math import gcd

# Encrypt one number (letter)
def encrypt(e1, e2, r, m, p):
    ct1 = pow(e1, r, p)
    ct2 = (m * pow(e2, r)) % p
    return ct1, ct2

# Decrypt one number (letter)
def decrypt(ct1, ct2, p, d):
    s = pow(ct1, d, p)
    s_inv = pow(s, p-2, p)   # modular inverse (Fermat)
    m = (ct2 * s_inv) % p
    return m

# Convert character → number  (a=0 ... z=25)
def char_to_num(ch):
    return ord(ch) - ord('a')

# Convert number → character
def num_to_char(n):
    return chr(n + ord('a'))


# -----------------------------
# MAIN PROGRAM
# -----------------------------
p = int(input("Enter a large prime p: "))
e1 = int(input("Select primitive root e1: "))
d = int(input("Enter private key d (1 < d < p-2): "))

# Compute public key
e2 = pow(e1, d, p)
print("Public key e2:", e2)

r = int(input("Enter random number r: "))

plaintext = input("Enter message (letters only): ").lower()

ciphertext = []
for ch in plaintext:
    m = char_to_num(ch)
    ct1, ct2 = encrypt(e1, e2, r, m, p)
    ciphertext.append((ct1, ct2))

print("Ciphertext pairs:", ciphertext)

# Decrypt back
decrypted = ""
for ct1, ct2 in ciphertext:
    m = decrypt(ct1, ct2, p, d)
    decrypted += num_to_char(m)

print("Decrypted text:", decrypted)

# Enter a large prime p: 31
# Select primitive root e1: 2
# Enter private key d (1 < d < p-2): 7
# Public key e2: 4
# Enter random number r: 5
# Enter message (letters only): hello
# Ciphertext pairs: [(1, 7), (1, 4), (1, 11), (1, 11), (1, 14)]
# Decrypted text: hello