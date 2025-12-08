import math
import numpy as np
import sympy as sp

def create_blocks(m,n):
    while len(m)%n!=0:
        m+='x'
    return [m[i:i+n] for i in range(0,len(m),n)]
    

def create_key_matrix(key,n):
    matrix = []
    k = 0
    for i in range(n):
        row=[]
        for j in range(n):
            if k < len(key):
                row.append(ord(key[k])-97)
                k+=1
        matrix.append(row)
    
    return np.array(matrix)

def create_inv_matrix(key_m,m=26):
    try:
        inv_key = sp.Matrix(key_m).inv_mod(m)
        return np.array(inv_key).astype(int)
    
    except:
        raise ValueError("Matrix is not invertible under modulo 26") 
    

def Encryption(m,key,n):
    blocks = create_blocks(m,n)
    key_m = create_key_matrix(key,n)
    matrix = []
    for block in blocks:
        row =[ord(c)-97 for c in block]
        matrix.append(row)
    matrix=np.array(matrix)

    ct=""
    for row in matrix:
        result = np.dot(row,key_m)%26
        for val in result.flatten():
            ct+=chr(int(val)+65)
    
    return ct

def Decryption(m,key,n):
    blocks = create_blocks(m,n)
    key_m = create_key_matrix(key,n)
    keym_inv = create_inv_matrix(key_m)
    matrix = []
    for block in blocks:
        row =[ord(c)-97 for c in block]
        matrix.append(row)
    matrix=np.array(matrix)

    ct=""
    for row in matrix:
        result = np.dot(row,keym_inv)%26
        for val in result.flatten():
            ct+=chr(int(val)+97)
    
    return ct


def Input(s):
    m = input(f"Enter {s}: ")
    key = input("Enter key: ")
    if not key.isalpha() or len(key)==0:
        print("Invalid key")
        return "",""
    if not m.isalpha() or len(m) == 0:
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
        n = int(math.sqrt(len(key)))

        if n*n != len(key):
            print("Length of key must be a perfect square")
            continue
       
        ct = Encryption(m.lower(),key.lower(),n)
        print("Cipher Text: ",ct)
    
    elif c == 2:
        m,key = Input("Ciphertext")
        if m == "" and key == "":
            continue
        n = int(math.sqrt(len(key)))
        if n*n != len(key):
            print("Length of key must be a perfect square")
            continue

        pt = Decryption(m.lower(),key.lower(),n)
        print("Plain Text: ",pt)
    
    elif c == 3:
        print("Exiting")
        break

    else:
        print("Invalid choice")
        continue
