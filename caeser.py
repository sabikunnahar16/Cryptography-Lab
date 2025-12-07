def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():  # only letters
            base = ord('a')
            # Shift and convert to uppercase
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            result += encrypted_char.upper()
        else:
            result += char  
    return result


def decrypt(cipher_text, shift):
    result = ""

    for char in cipher_text:
        if char.isalpha():
            base = ord('A')
            # Shift backward and convert to lowercase
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            result += decrypted_char.lower()
        else:
            result += char
    return result



plaintext = "hello"
shift_value = 3

cipher = encrypt(plaintext, shift_value)
plain = decrypt(cipher, shift_value)

print("Plaintext :", plaintext)
print("Encrypted :", cipher)
print("Decrypted :", plain)
