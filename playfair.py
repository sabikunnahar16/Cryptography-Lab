import string



def generate_key_table(key):
    key = key.lower().replace("j", "i")  # I/J together
    result = []
    used = set()

    # Add key letters
    for ch in key:
        if ch in string.ascii_lowercase and ch not in used:
            used.add(ch)
            result.append(ch)

    # Add remaining alphabet
    for ch in string.ascii_lowercase:
        if ch == "j":
            continue
        if ch not in used:
            result.append(ch)

    # Build 5x5 matrix
    matrix = [result[i:i+5] for i in range(0, 25, 5)]
    return matrix


def find_position(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
    return None


def process_text(text):
    text = text.lower().replace(" ", "").replace("j", "i")
    prepared = ""
    i = 0

    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i+1]
            if a == b:
                prepared += a + "x"
                i += 1
            else:
                prepared += a + b
                i += 2
        else:
            prepared += a + "x"
            i += 1

    return prepared


def encrypt_pair(a, b, matrix):
    r1, c1 = find_position(matrix, a)
    r2, c2 = find_position(matrix, b)

    if r1 == r2:  
        return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
    elif c1 == c2:  
        return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
    else:  # Rectangle rule
        return matrix[r1][c2] + matrix[r2][c1]


def decrypt_pair(a, b, matrix):
    r1, c1 = find_position(matrix, a)
    r2, c2 = find_position(matrix, b)

    if r1 == r2:  # Same row
        return matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
    elif c1 == c2:  # Same column
        return matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
    else:  # Rectangle rule
        return matrix[r1][c2] + matrix[r2][c1]


def clean_decrypted(text):
    cleaned = ""

    i = 0
    while i < len(text):
        # Remove inserted "x" between repeated letters
        if i < len(text)-2 and text[i] == text[i+2] and text[i+1] == "x":
            cleaned += text[i]
            i += 2
        else:
            cleaned += text[i]
            i += 1

    # Remove ending "x"
    if cleaned.endswith("x"):
        cleaned = cleaned[:-1]

    return cleaned


# ---------- MAIN PROGRAM ----------

while True:
    mode = input("Encrypt or Decrypt? ").lower()
    text = input("Enter text: ").lower()
    key = input("Enter key: ").lower()

    matrix = generate_key_table(key)

    if mode == "encrypt":
        prepared = process_text(text)
        cipher = ""
        for i in range(0, len(prepared), 2):
            cipher += encrypt_pair(prepared[i], prepared[i+1], matrix)
        print("Encrypted:", cipher)

    else:
        text = text.replace(" ", "")
        plain = ""
        for i in range(0, len(text), 2):
            plain += decrypt_pair(text[i], text[i+1], matrix)
        print("Decrypted:", clean_decrypted(plain))

    cont = input("Continue? Yes/No: ").lower()
    if cont != "yes":
        break