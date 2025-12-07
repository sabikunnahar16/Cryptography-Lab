


def auto_key_cipher_encription(text, key):
    cipher_text = ""
    for char in text:
        if char.isalpha():
            shift = ((ord(char)-ord('a'))+key)%26
            cipher_text+=chr(shift + ord('a')).upper()
            key = ord(char) - ord('a')
        else:
            continue
    
    return cipher_text
    

def auto_key_cipher_decryption(text, key):
    plaintext = ""

    for char in text:
        if char.isalpha():
            shift = ((ord(char)-ord('A'))-key)%26
            plaintext += chr(shift + ord('A')).lower()
            key = shift
        
        else:
            continue
    
    return plaintext

if __name__ == "__main__":
        

        while True:
            print("Slect an option: ")
            print("1. Encryption")
            print("2. Decryption")
            print("3. Use your own name's length for key generation: ")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                text = input("Enter the text to encrypt: ")
                key = int(input("Enter the key value: "))
                print("Encrypted text: ", auto_key_cipher_encription(text, key))
                  
            elif choice == '2':
                text = input("Enter the text to decrypt: ")
                key = int(input("Enter key value: "))
                print("Decrypted text: ", auto_key_cipher_decryption(text, key))

            
            elif choice == '3':
                name = input("Enter your name: ")
                text = input("Enter the text to encrypt: ")
                print("Encrypted text: ", auto_key_cipher_encription(text, len(name)))
                


            elif choice == '4':
                print("Exiting...")
                break

            else:
                print("Invalid choice, please try again.")
                continue


        
