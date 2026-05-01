# # RSA Cycling Attack for e = 3, n = 35, ciphertext = 22

# e = 3
# n = 35
# ciphertext = 22

# def rsa_encrypt(x, e, n):
#     return pow(x, e, n)

# # Perform cycling attack
# value = ciphertext
# seen = set()

# print("Starting cycling attack...\n")

# for i in range(1, 50):   # Enough iterations for cycling
#     value = rsa_encrypt(value, e, n)
#     print(f"Cycle {i}: {value}")
    
#     if value in seen:
#         print("\nCycle repeated! Loop detected.")
#         break
#     seen.add(value)
# print("\nCycling attack completed.")
# ======================================================
# RSA Cycling Attack Demonstration
# Public Key: e = 3, n = 35
# Ciphertext: C = 22
# ======================================================

# RSA Cycling Attack
# Public key: e = 3, n = 35
# Ciphertext: C = 22

e = 3
n = 35
C = 22

def rsa_encrypt(x):
    return pow(x, e, n)

print("Starting Cycling Attack...\n")
print(f"Ciphertext: {C}\n")

value = C
seen = set()

for i in range(1, 10):
    value = rsa_encrypt(value)
    print(f"Cycle {i}: {value}")

    # If the value becomes the ciphertext again, plaintext found
    if value == C:
        print("\nPlaintext found!")
        print(f"Plaintext = {value}")
        break
