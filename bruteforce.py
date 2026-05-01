def affain_cipher_encrypt(text, shift1, shift2):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a')
            p = ord(char) - base
            c =  (p * shift1 + shift2) % 26
            result += chr(base + c)
        else :
            result += char
    return result.upper()

def affain_cipher_decrypt(text, shift1, shift2):
    r1 = 26
    r2 = shift1
    t1 = 0
    t2 = 1
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        r1 = r2
        r2 = r

        t = t1  - q * t2
        t1 = t2
        t2 = t
    
    if r1 !=  1:
        return "shift1 value is not coprime with 26 , decryption not possible."

    shift1_inverse = t1 % 26

    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A')
            c = ord(char) - base
            p = ((c - shift2) * shift1_inverse) % 26
            result += chr(base + p)
        
        else:
            result += char
    return result.lower()


if __name__ == "__main__":

    while True:
        print("Select an option: ")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Unknown first key value to decrypt")
        print("4. Unknown second key value to decrypt")
        print("5. Unknown both key values to decrypt")
        print("6. Exit")

        choice = input("Enter your choice: ")
        

        if choice == '1':
            pt = input("Enter the text to encrypt: ")
            shift1 = int(input("Enter the first shift value: "))
            shift2 = int(input("Enter the second shift value: "))
            print("Encrypted text: ", affain_cipher_encrypt(pt.lower(), shift1, shift2))


        elif choice == '2':
            ct = input("Enter the text to decrypt: ")
            shift1 = int(input("Enter the first shift value: "))
            shift2 = int(input("Enter the second shift value: "))
            print("Decrypted text: ", affain_cipher_decrypt(ct.upper(), shift1, shift2))
        
        

        elif choice == '3':
            ct = input("Enter the text to decrypt: ")
            shift2 = int(input("Enter the second shift value: "))
            for shift1 in range(1,26):
                print(f"shift1 {shift1}: {affain_cipher_decrypt(ct.upper(), shift1, shift2)}")
            
        elif choice == '4':
            ct = input("Enter the text to decrypt: ")
            shift1 = int(input("Enter the first shift value: "))
            for shift2 in range(1,26):
                print(f"shift2 {shift2}: {affain_cipher_decrypt(ct.upper(), shift1, shift2)}")

        elif choice == '5':
            ct = input("Enter the text to decrypt: ")
            for shift1 in range(1,26):
                for shift2 in range(1,26):
                    print(f"Shift1={shift1}, Shift2={shift2}: {affain_cipher_decrypt(ct.upper(), shift1, shift2)}")


        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
            continue