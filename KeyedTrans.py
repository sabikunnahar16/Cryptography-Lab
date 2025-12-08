# def generate_key_order(key):
   
#     key = key.lower()
#     sorted_key = sorted(list(key))
#     order = []

#     for char in key:
#         order.append(sorted_key.index(char))
#         sorted_key[sorted_key.index(char)] = "_"   

#     return order


# def encrypt_keyed_transposition(plaintext, key):
#     plaintext = plaintext.replace(" ", "").lower()
#     cols = len(key)

   
#     rows = len(plaintext) // cols
#     if len(plaintext) % cols != 0:
#         rows += 1

   
#     matrix = [["" for _ in range(cols)] for _ in range(rows)]

#     # fill row-wise
#     index = 0
#     for r in range(rows):
#         for c in range(cols):
#             if index < len(plaintext):
#                 matrix[r][c] = plaintext[index]
#                 index += 1
#             else:
#                 matrix[r][c] = "x"   

#     # calculate key order
#     order = generate_key_order(key)

#     # read column-wise based on key order
#     ciphertext = ""
#     for col_num in range(len(order)):
#         col_index = order.index(col_num)
#         for r in range(rows):
#             ciphertext += matrix[r][col_index].upper()

#     return ciphertext


# def decrypt_keyed_transposition(ciphertext, key):
#     ciphertext = ciphertext.replace(" ", "").upper()
#     cols = len(key)

#     # determine rows
#     rows = len(ciphertext) // cols

  
#     matrix = [["" for _ in range(cols)] for _ in range(rows)]

#     # get key order
#     order = generate_key_order(key)

#     # fill columns based on key order
#     index = 0
#     for col_num in range(len(order)):
#         col_index = order.index(col_num)
#         for r in range(rows):
#             matrix[r][col_index] = ciphertext[index].lower()
#             index += 1

  
#     plaintext = ""
#     for r in range(rows):
#         for c in range(cols):
#             plaintext += matrix[r][c]

#     return plaintext.rstrip("x")   


# if __name__ == "__main__":
#     while True:
#         print("Select an option:")
#         print("1. Encrypt (Keyed Transposition)")
#         print("2. Decrypt (Keyed Transposition)")
#         print("3. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             pt = input("Enter the plaintext: ")
#             key = input("Enter the key: ")
#             print("Ciphertext:", encrypt_keyed_transposition(pt, key))

#         elif choice == "2":
#             ct = input("Enter the ciphertext: ")
#             key = input("Enter the key: ")
#             print("Plaintext:", decrypt_keyed_transposition(ct, key))

#         elif choice == "3":
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice, please try again.") 
import math

import numpy as np


def create_msg_matrix(m,n):
    while len(m)%n !=0:
        m+='z'
    l = len(m)
    k = math.ceil(l/n)
    h=0
    matrix = []
    for i in range(k):
        row=[]
        for j in range(n):
            if h<l:
                row.append(ord(m[h])-97)
                h+=1
        matrix.append(row)
    
    return np.array(matrix)


def create_key_matrix(key):
    n = len(key)
    k = 0
    matrix = np.zeros((n,n),dtype=int)
    perm = [int(d)-1 for d in key]

    for i in range(n):
        row = perm[i]
        matrix[row][i]=1
    
    return matrix

def create_inv_key_matrix(key):
    n = len(key)
    k = 0
    matrix = np.zeros((n,n),dtype=int)
    perm = [int(d)-1 for d in key]

    for i in range(n):
        col = perm[i]
        matrix[i][col]=1
    
    return matrix



def Encryption(m,key):
    m = m.replace(" ", "").lower()
    m_matrix = create_msg_matrix(m,len(key))
    key_matrix = create_key_matrix(key)
    result = np.dot(m_matrix,key_matrix)%26

    ct = ""
    k = math.ceil(len(m)/len(key))

    for i in range(k):
        for j in range(len(key)):
            ct+=chr(65+result[i][j])
    return ct

def Decryption(m,key):
    m = m.replace(" ", "").lower()
    m_matrix = create_msg_matrix(m,len(key))
    key_matrix = create_inv_key_matrix(key)
    result = np.dot(m_matrix,key_matrix)%26

    ct = ""
    k = math.ceil(len(m)/len(key))

    for i in range(k):
        for j in range(len(key)):
            ct+=chr(97+result[i][j])
    return ct


def Input(s):
    m = input(f"Enter {s}: ")
    key = input("Enter key: ")
    if len(key)<3:
        print("Invalid key")
        return "",""
    # allow spaces: validate letters after removing spaces
    cleaned = m.replace(" ", "")
    if not cleaned.isalpha() or len(cleaned) == 0:
        print("Please provide proper message")
        return "",""
    
    return m,key


while True:
    print("1.Encryption\n2.Decryption\n3.Exit")
    c = int(input("Enter an option: "))

    if c == 1:
        m,key = Input("Plaintext")
        if m == "" and key == "":
            continue
        ct = Encryption(m.lower(),key)
        print("Cipher Text: ",ct)
    
    elif c == 2:
        m,key = Input("Ciphertext")
        if m == "" and key == "":
            continue
        pt = Decryption(m.lower(),key)
        print("Plain Text: ",pt)
    
    elif c == 3:
        print("Exiting")
        break

    else:
        print("Invalid choice")
        continue
