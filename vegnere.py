def generate_key(text, key):
    key = key.lower()
    new_key = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            new_key += key[key_index % len(key)]
            key_index += 1
        else:
            new_key += char
    return new_key


def vigenere_encrypt(text, key):
    text = text.lower()
    key = generate_key(text, key)
    cipher = ""

    for t, k in zip(text, key):
        if t.isalpha():
            # Convert characters to 0–25 numbers
            shift = (ord(t) - ord('a') + (ord(k) - ord('a'))) % 26
            cipher += chr(shift + ord('A'))   # UPPERCASE
        else:
            cipher += t  # keep spaces/symbols

    return cipher


def vigenere_decrypt(cipher, key):
    cipher = cipher.upper()
    key = generate_key(cipher.lower(), key)
    plaintext = ""

    for c, k in zip(cipher, key):
        if c.isalpha():
            shift = (ord(c) - ord('A') - (ord(k) - ord('a'))) % 26
            plaintext += chr(shift + ord('a'))  # lowercase
        else:
            plaintext += c

    return plaintext


# ---------------- MAIN PROGRAM ----------------

if __name__ == "__main__":
    while True:
        print("\nVigenère Cipher Menu")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            text = input("Enter text to encrypt: ")
            key = input("Enter key: ")
            print("Encrypted Text:", vigenere_encrypt(text, key))

        elif choice == '2':
            cipher = input("Enter cipher text: ")
            key = input("Enter key: ")
            print("Decrypted Text:", vigenere_decrypt(cipher, key))

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")
