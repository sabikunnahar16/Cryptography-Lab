# -------------------- Polybius Square --------------------
# Classic 5×5 square, I/J treated as same
polybius_square = [
    ["a", "b", "c", "d", "e"],
    ["f", "g", "h", "i", "k"],  # i = j
    ["l", "m", "n", "o", "p"],
    ["q", "r", "s", "t", "u"],
    ["v", "w", "x", "y", "z"]
]

# Create dictionaries for fast lookup
letter_to_code = {}
code_to_letter = {}

for row in range(5):
    for col in range(5):
        letter = polybius_square[row][col]
        code = f"{row+1}{col+1}"  # coordinates start from 1
        letter_to_code[letter] = code
        code_to_letter[code] = letter


# -------------------- Encryption --------------------
def polybius_encrypt(text):
    text = text.lower().replace("j", "i").replace(" ", "")
    cipher = ""

    for char in text:
        if char.isalpha():
            cipher += letter_to_code[char] + " "
    
    return cipher.strip()


# -------------------- Decryption --------------------
def polybius_decrypt(cipher):
    cipher = cipher.replace(" ", "")
    plaintext = ""

    # Read 2 digits at a time
    for i in range(0, len(cipher), 2):
        code = cipher[i:i+2]
        if code in code_to_letter:
            plaintext += code_to_letter[code]
    
    return plaintext


# -------------------- Main Program --------------------
if __name__ == "__main__":
    while True:
        mode = input("Encrypt or Decrypt? ").lower()

        if mode == "encrypt":
            text = input("Enter text: ")
            print("Encrypted:", polybius_encrypt(text))

        elif mode == "decrypt":
            text = input("Enter Cipher (pairs like '11 21 35'): ")
            print("Decrypted:", polybius_decrypt(text))

        else:
            print("Invalid mode!")

        cont = input("Continue? yes/no: ").lower()
        if cont != "yes":
            break
