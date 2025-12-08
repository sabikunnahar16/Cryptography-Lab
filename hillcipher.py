import numpy as np

# Convert char to number
def char_to_num(c):
    return ord(c) - ord('a')

# Convert number to char
def num_to_char(n):
    return chr((n % 26) + ord('a'))

# Modular inverse for determinant
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Encryption
def hill_encrypt(plaintext, key):
    n = len(key)
    plaintext = plaintext.replace(" ", "").lower()

    # Pad text if needed
    while len(plaintext) % n != 0:
        plaintext += "z"

    plaintext_vecs = []
    for i in range(0, len(plaintext), n):
        vec = [char_to_num(c) for c in plaintext[i:i+n]]
        plaintext_vecs.append(vec)

    ciphertext = ""

    for vec in plaintext_vecs:
        result = np.dot(key, vec) % 26
        for num in result:
            ciphertext += num_to_char(num).upper()

    return ciphertext


# Decryption
def hill_decrypt(ciphertext, key):
    n = len(key)
    ciphertext = ciphertext.replace(" ", "").upper()

    # Compute determinant
    det = int(round(np.linalg.det(key)))
    det = det % 26

    det_inv = mod_inverse(det, 26)
    if det_inv is None:
        return "ERROR: Key matrix is not invertible modulo 26!"

    # Matrix adjoint
    adj = np.round(det * np.linalg.inv(key)).astype(int) % 26

    # Inverse key matrix mod 26
    inv_key = (det_inv * adj) % 26

    plaintext = ""

    for i in range(0, len(ciphertext), n):
        vec = [char_to_num(c.lower()) for c in ciphertext[i:i+n]]
        result = np.dot(inv_key, vec) % 26

        for num in result:
            plaintext += num_to_char(num)

    return plaintext




n = int(input("Enter matrix size (n for n×n): "))

print("Enter your key matrix values row by row:")

key_matrix = []
for i in range(n):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    key_matrix.append(row)

key_matrix = np.array(key_matrix)

print("\n1. Encrypt")
print("2. Decrypt")
choice = input("Choose: ")

if choice == "1":
    text = input("Enter plaintext: ")
    print("Ciphertext:", hill_encrypt(text, key_matrix))

elif choice == "2":
    text = input("Enter ciphertext: ")
    print("Plaintext:", hill_decrypt(text, key_matrix))

else:
    print("Invalid option.")
# Row 1: 9 7 11 13
# Row 2: 4 7 5 6
# Row 3: 2 21 14 9
# Row 4: 3 23 21 8  code is ready