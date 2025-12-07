
def caesar_cipher_encryption(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a')
            p = ord(char) - base
            c = (p + shift) % 26
            result += chr(base + c)
        else:
            result += char
    return result.upper()

def caesar_cipher_decryption(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A')
            c = ord(char) - base
            p = (c - shift) % 26
            result += chr(p + base)
        else:
            result += char
    return result.lower()


if __name__ == "__main__":

    while True:

        print("Select an option: ")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Unknown key value to decrypt")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            pt = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            print("Encrypted text: ", caesar_cipher_encryption(pt.lower(), shift))
        elif choice == '2':
            ct = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            print("Decrypted text: ", caesar_cipher_decryption(ct.upper(), shift))
        
        elif choice == '3':
            ct = input("Enter the text to decrypt: ")
            for shift in range(1,26):
                print(f"Shift {shift}: {caesar_cipher_decryption(ct.upper(), shift)}")

        
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
            continue

    
