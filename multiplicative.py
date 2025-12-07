
def mod_inverse(key, m=26):
    for i in range(1, m):
        if (key * i) % m == 1:
            return i
    return None


def encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            
            char = char.lower()

            p = ord(char) - ord('a')      
            c = (p * key) % 26             
            result += chr(c + ord('A'))     
        else:
            result += char
    return result


def decrypt(cipher, key):
    result = ""
    key_inv = mod_inverse(key)

    if key_inv is None:
        return "Error: key has no inverse. Choose another key."

    for char in cipher:
        if char.isalpha():
            c = ord(char) - ord('A')       
            p = (c * key_inv) % 26          
            result += chr(p + ord('a'))     
        else:
            result += char
    return result



plaintext = "hello"
key = 7

cipher = encrypt(plaintext, key)
plain = decrypt(cipher, key)

print("Input text :", plaintext)
print("Ciphertext :", cipher)
print("Decrypted  :", plain)
