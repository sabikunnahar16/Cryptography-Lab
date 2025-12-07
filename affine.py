
def mod_inverse(a, m=26):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def encrypt(text, a, b):
    result = ""

    for char in text:
        if char.isalpha():
            char = char.lower()  

            p = ord(char) - ord('a')        
            c = (a * p + b) % 26           
            result += chr(c + ord('A'))     
        else:
            result += char
    return result


def decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a)

    if a_inv is None:
        return "Error: 'a' has no modular inverse. Choose a valid key."

    for char in cipher:
        if char.isalpha():
            c = ord(char) - ord('A')            
            p = (a_inv * (c - b)) % 26          
            result += chr(p + ord('a'))         
        else:
            result += char
    return result


plaintext = "math"
a = 3    
b = 7    

cipher = encrypt(plaintext, a, b)
plain = decrypt(cipher, a, b)

print("Input Text :", plaintext)
print("Ciphertext :", cipher)
print("Decrypted  :", plain)
